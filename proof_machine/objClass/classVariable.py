class Variable:
	def __init__(self, name, ptype = 'symbol', state = None, latex = None):
		self.name = name
		self.type = ptype
		if state != None and getClass(state) != 'list':
			raise ValueError("state must be of type 'list'.")
		self.state = state
		if latex == None:
			self.latex = name
		else:
			self.latex = latex

	def modify(self, attr, newValue):
		if attr not in ['name', 'type', 'state', 'latex']:
			raise ValueError(attr + "is not a value attributes. It must be one of 'name', 'type', 'state' and 'latex'.")
		else:
			self[attr] = newValue

	def View(self):
		stateStr = '' if self.state == None else ", ".join(self.state)
		latexStr = '' if self.latex == None else self.latex
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format(self.name, self.type, stateStr, latexStr))

class Namespace:
	def __init__(self):
		self.variableList = []
		self.addDefault()

	def addDefault(self):
		self.defineVariable('parentheses', ['{', '[', '(', ')', ']', '}'])

	def defineVariable(self, ptype, varName):
		# Interface to handle list input or single input.
		for var in varName:	
			self.addVariable(Variable(var, ptype))
	
	def addVariable(self, newVariable):
		if self.isExist(newVariable.name):
			raise ValueError("Variable " + newVariable.name + " already exists.")
		else:
			self.variableList.append(newVariable)

	def modifyVariable(self, varName, attr, newValue):
		if not isExist(newVariable):
			raise ValueError("Cannot modify a variable that doesn't exist.")
		else:
			for var in self.variableList:
				if var.name == varName:
					var.modify(attr, newValue)

	def isExist(self, varName):
		any([x.name == varName for x in self.variableList])

	def View(self):
		print("{:>15} \t {:>12} \t {:>15} \t {:>12}".format("Variable", "Parse type", "State", "Latex"))
		for var in self.variableList:
			var.View() 
