from proof_machine.others import default_namespace, getClass

class Variable:
	""" represents mathematical symbols / variables. 

	Attributes:
		name (str), state (list of str), latex (str), ptype (str): one of 'symbol', 'function', 'operator', 'parentheses'
	"""
	def __init__(self, name, ptype = 'symbol', state = None, latex = None):
		self.name = name
		self.ptype = ptype
		if state != None and getClass(state) != 'list':
			raise ValueError("state must be of type 'list'.")
		self.state = state
		self.latex = name if latex is None else latex

	def View(self):
		""" Print outs all the attributes of the object """
		stateStr = '' if self.state == None else ", ".join(self.state)
		latexStr = '' if self.latex == None else self.latex
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format(self.name, self.ptype, stateStr, latexStr))

	# Internal generic attributes setter
	def modify(self, attr, newValue):
		""" Internal generic attributes setter """
		if attr not in ['name', 'ptype', 'state', 'latex']:
			raise ValueError(attr + " is not a valid attribute. It must be one of 'name', 'ptype', 'state' and 'latex'.")
		else:
			setattr(self, attr, newValue)


class Namespace:
	""" keeps track of all the mathematical variables defined. 
	
	Attributes: 
		variableList (list of Variable).
	"""
	
	def __init__(self):
		self.variableList = []
		self.addDefault()


	# Variables related
	def addDefault(self):
		""" adds some commonly used variables. """
		self.defineVariable('parentheses', default_namespace()['parentheses'])
		self.defineVariable('operator', default_namespace()['arithmeticOperator'])
		self.defineVariable('operator', default_namespace()['setOperator'])

	
	def defineVariable(self, ptype, varName, state = None, latex = None):	
		""" defines new mathematical variable and adds to the variableList. 
		
		Args:
			ptype (str), varName (str or list of str), state (list of str), latex (str)

		Note:		
        	if varName is a list, then state and latex variables are ignored.

		Examples:

				>>> import string

		    	>>> globalVariables = Namespace()
				
				Input a list for varName:

		    	>>> globalVariables.defineVariable('symbol', list(string.ascii_lowercase) + list(string.ascii_uppercase))
				
				Usual usage for varName:

		    	>>> globalVariables.defineVariable('symbol', 'X1', ['random variable'], 'X_1	')
				
				>>> globalVariables.View()
		"""

		if varName.__class__.__name__ == 'list':
			for var in varName:	
				self.addVariable(Variable(var, ptype, None, None))
		else:
			self.addVariable(Variable(varName, ptype, state, latex))
	

	def findVariable(self, varName):
		""" finds a variable by name and returns it if found """
		for x in self.variableList:
			if x.name == varName:
				return x


	def addVariable(self, newVariable):
		""" adds a variable to the variableList"""
		if self.isExist(newVariable.name):
			raise ValueError("Variable " + newVariable.name + " already exists.")
		else:
			self.variableList.append(newVariable)


	def modifyVariable(self, varName, attr, newValue):
		""" [internal] modifies a variable's attribute """
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			[var.modify(attr, newValue) for var in self.variableList if var.name == varName]


	# State related
	def addState(self, varName, newValue):
		""" adds a state to a variable in the variableList"""
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			var = self.findVariable(varName)
			if var:
				var.state = [newValue] if var.state is None else var.state + [newValue]


	def removeState(self, varName, newValue):
		""" removes a state from a variable in the variableList"""
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			var = self.findVariable(varName)
			var.state.remove(newValue)


	def isExist(self, varName):
		""" checks if a variable exists (by name) """
		return any([x.name == varName for x in self.variableList])


	def View(self):
		""" prints out each variable in the variableList. """
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format("Variable", "Parse type", "State", "Latex"))
		[var.View() for var in self.variableList]	

			
# Helper functions
def lookupPtype(varName, namespace):
	""" Helper function to look up the variable type in a given namespace """
	res = namespace.findVariable(varName)
	return res.ptype if res else 'undefined'


def lookup_state(varName, namespace):
	""" Helper function to look up the variable state in a given namespace """
	res = namespace.findVariable(varName)
	return res.state if res else 'undefined'
