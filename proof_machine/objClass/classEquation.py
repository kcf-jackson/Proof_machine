class Equation:
	# The Equation class has trees on both sides and an operator in-between.
	def __init__(self, LHS, OP, RHS):
		self.lhs = LHS
		self.op = OP
		self.rhs = RHS

	def changeOp(self, op):
		self.op = op
		self.view()
		
	def view(self):
		print(treeToString(self.lhs) + ' ' + self.op + ' '+ treeToString(self.rhs))

	def applyToLeft(self, f, *args):
		if args:
			self.lhs = f(self.lhs, args[0])
		else:
			self.lhs = f(self.lhs)
		self.view()

	def applyToRight(self, f, *args):
		if args:
			self.rhs = f(self.rhs, args[0])
		else:
			self.rhs = f(self.rhs)
		self.view()

	def applyToBoth(self, f, *args):
		if args:
			self.lhs = f(self.lhs, args[0])
			self.rhs = f(self.rhs, args[0])
		else:
			self.lhs = f(self.lhs)
			self.rhs = f(self.rhs)
		self.view()

	def switchLeftAndRight(self):
		oppositeDict = {'=': '=', '<': '>', '>':'<', '>=':'<=', '<=':'>='}
		self.lhs, self.rhs = self.rhs, self.lhs
		self.op = oppositeDict[self.op]

def transitive(eq1, eq2):
	if eq1.op not in ['=', '<', '<=']:
		eq1.switchLeftAndRight()
	if eq2.op not in ['=', '<', '<=']:	
		eq2.switchLeftAndRight()
	if treeToString(eq1.rhs) == treeToString(eq2.lhs):
		return Equation(eq1.lhs, combineOp(eq1.op, eq2.op), eq2.rhs)
	elif treeToString(eq2.rhs) == treeToString(eq1.lhs):
		return Equation(eq2.lhs, combineOp(eq1.op, eq2.op), eq1.rhs)
	else:
		print("Cannot combine two equations.")
		return None

def combineOp(op1, op2):
	opDict = {'<': 0,'<=': 1}
	revDict = {value: key for key, value in opDict.items()}
	return revDict[opDict[op1] * opDict[op2]]
