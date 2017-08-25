class ExprTuple:
	def __init__(self, expr):
		self.lhs = str(expr[0])
		self.op = str(expr[1])
		self.rhs = str(expr[2])

	def takeExpectation(self):
		self.lhs = "E[" + self.lhs + "]"
		self.rhs = "E[" + self.rhs + "]"

	def add(self, r):
		self.lhs += "+" + str(r)
		self.rhs += "+" + str(r)

	def sub(self, r):
		self.lhs += "-" + str(r)
		self.rhs += "-" + str(r)

	def mul(self, r):
		self.lhs += "*" + str(r)
		self.rhs += "*" + str(r)

	def div(self, r):
		self.lhs += "/" + str(r)
		self.rhs += "/" + str(r)

	def view(self):
		print(self.lhs + self.op + self.rhs)

	def eval(self):
		self.lhs = str(eval(self.lhs))
		self.rhs = str(eval(self.rhs))
		if (eval(self.lhs) > eval(self.rhs)):
			self.op = ">"
		self.view()

eq1 = ExprTuple(['3', '<=', '4'])
eq1.view()

eq1.add('1')
eq1.view()
eq1.eval()

eq1.mul('2')
eq1.view()
eq1.eval()

eq1.mul('-1')
eq1.view()
eq1.eval()

eq2 = ExprTuple(['a', '<=', 'b'])
eq2.view()

eq2.add('1')
eq2.view()

eq3 = ExprTuple(['a * I_{X>=a}', '<=', 'X'])
eq3.view()
eq3.takeExpectation()
eq3.view()
