from proof_machine.others import dafaultNamespace, getClass

class Variable:
	def __init__(self, name, ptype = 'symbol', state = None, latex = None):
		self.name = name
		self.ptype = ptype
		if state != None and getClass(state) != 'list':
			raise ValueError("state must be of type 'list'.")
		self.state = state
		if latex == None:
			self.latex = name
		else:
			self.latex = latex

	def modify(self, attr, newValue):
		if attr not in ['name', 'ptype', 'state', 'latex']:
			raise ValueError(attr + " is not a valid attribute. It must be one of 'name', 'ptype', 'state' and 'latex'.")
		else:
			setattr(self, attr, newValue)

	def View(self):
		stateStr = '' if self.state == None else ", ".join(self.state)
		latexStr = '' if self.latex == None else self.latex
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format(self.name, self.ptype, stateStr, latexStr))

class Namespace:
	def __init__(self):
		self.variableList = []
		self.addDefault()

	def addDefault(self):
		self.defineVariable('parentheses', dafaultNamespace()['parentheses'])
		self.defineVariable('operator', dafaultNamespace()['arithmeticOperator'])
		self.defineVariable('operator', dafaultNamespace()['setOperator'])

	def defineVariable(self, ptype, varName):
		# Interface to handle list input or single input.
		if varName.__class__.__name__ == 'list':
			for var in varName:	
				self.addVariable(Variable(var, ptype, []))
		else:
			self.addVariable(Variable(varName, ptype, []))
	
	def addVariable(self, newVariable):
		if self.isExist(newVariable.name):
			raise ValueError("Variable " + newVariable.name + " already exists.")
		else:
			self.variableList.append(newVariable)

	def modifyVariable(self, varName, attr, newValue):
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			for var in self.variableList:
				if var.name == varName:
					var.modify(attr, newValue)

	def addState(self, varName, newValue):
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			for var in self.variableList:
				if var.name == varName:
					var.state = var.state + [newValue]

	def removeState(self, varName, newValue):
		if not self.isExist(varName):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			for var in self.variableList:
				if var.name == varName:
					var.state.remove(newValue)

	def findVariable(self, varName):
		for x in self.variableList:
			if x.name == varName:
				return x

	def isExist(self, varName):
		return any([x.name == varName for x in self.variableList])

	def View(self):
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format("Variable", "Parse type", "State", "Latex"))
		for var in self.variableList:
			var.View() 

# Helper functions
def lookupPtype(varName, namespace):
    res = namespace.findVariable(varName)
    return res.ptype if res else 'undefined'

def lookupState(varName, namespace):
    res = namespace.findVariable(varName)
    return res.state if res else 'undefined'
