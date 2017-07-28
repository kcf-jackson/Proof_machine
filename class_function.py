class Indicator():
	def __init__(self, h = 'b', a = 'a'):
		self.jumpAt = a
		self.value = h

	def view(self):
		if str(self.value) == '1':
			print("1_{X >= " + str(self.jumpAt) + "}")
			return "1_{X >= " + str(self.jumpAt) + "}"	
		print(str(self.value) + " * 1_{X >= " + str(self.jumpAt) + "}")
		return str(self.value) + " * 1_{X >= " + str(self.jumpAt) + "}"

	def geq(self, f2, axiomList):
		if getClass(self) == getClass(f2):
			return firstGeqSecond(self.value, f2.value, axiomList) and \
					firstLeqSecond(self.jumpAt, f2.jumpAt, axiomList)
		else:
			return None

	def leq(self, f2, axiomList):
		if getClass(self) == getClass(f2):
			return firstLeqSecond(self.value, f2.value, axiomList) and \
					firstGeqSecond(self.jumpAt, f2.jumpAt, axiomList)
		else:
			if getClass(f2) == "Monomial":
				return firstLeqSecond(self.value, self.jumpAt, axiomList)
			else:
				return None

class Simple():
	def __init__(self, listJumpAt, listValue):
		self.jumpAt = listJumpAt
		self.value = listValue

class Monomial():
	def __init__(self, exp = '1'):
		self.exponent = exp
	
	def view(self):
		if str(self.exponent) == '1':
			print("X")
			return "X"
		print("X^" + str(self.exponent))
		return "X^" + str(self.exponent)

