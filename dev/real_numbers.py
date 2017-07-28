class Real():
	def __init__(self, value):
		self.value = value

	def add(self, r):
		res = Real()
		res.value = self.value + r.value
		return res


class Real():
	def __init__(self, value, state = None):
		self.value = value
		self.evaluable = None
		self.isEvaluable()		

		if self.evaluable == False:
			self.state = state
		else:
			if self.value == 'Inf':
				self.state = "positive"
			elif self.value == '-Inf':
				self.state = "negative"
			else:
				if float(self.value) > 0:
					self.state = "positive"
				elif float(self.value) < 0:
					self.state = "negative"
				elif float(self.value) == 0:
					self.state = "zero"
				else:
					self.state = None

	def isEvaluable(self):
		if self.value in ['Inf', '-Inf']:
			self.evaluable = True
		else:
			try:
				b = float(self.value)
				self.evaluable = True
			except ValueError:
				self.evaluable = False

	# Functions for checking the state object	
	def isNonNegative(self):
		return isZero(self) or isPositive(self)

	def isNonPositive(self):
		return isZero(self) or isNegative(self)

	def isZero(self):
		return self.state == "zero"

	def isPositive(self):
		return self.state == "positive"

	def isNegative(self):
		return self.state == "negative"
	
	def add(self, a0):
		self.value = self.value + a0.value
 

import unittest
class TestStringMethods(unittest.TestCase):
    def test_Real(self):
        self.assertTrue(Real('-3').evaluable)
        self.assertTrue(Real(3).evaluable)
        self.assertTrue(Real("Inf").evaluable)
        self.assertTrue(Real("-Inf").evaluable)
        self.assertFalse(Real("a").evaluable)

if __name__ == '__main__':
    unittest.main()

	
	# def minus(self, b):
	# 	self.value = str(float(self.value) - float(b))
	# def multiply(self, b):	
	# 	self.value = str(float(self.value) * float(b))	
	# def division(self, b):
	# 	if str(b) == '0.0' or str(b) == '0':
	# 		if self.value == 'Inf':
	# 			self.value = 
	# 	self.value = str(float(self.value) / float(b))
