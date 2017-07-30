class Equation:
	def __init__(self, LHS, OP, RHS):
		self.lhs = LHS
		self.op = OP
		self.rhs = RHS

	def view(self):
		print(treeToString(self.lhs) + ' ' + self.op + ' '+ treeToString(self.rhs))

	def applyToLeft(self, f, ...):
		self.lhs = f(self.lhs)

	def applyToRight(self, f, ...):
		self.rhs = f(self.rhs)
