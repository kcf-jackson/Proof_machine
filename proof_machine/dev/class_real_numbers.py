class Real():
	def __init__(self, value = "", state = None):
		self.value = str(value)
		self.state = state
		self.evaluated = False

	def __add__(self, r):
		res = Real()
		res.value = str(self.value) + "+" + str(r.value)
		if res.value == "+":
			res.value = ""
		if self.state == "positive" and r.state == "positive":
			res.state = "positive"
		elif self.state == "negative" and r.state == "negative":
			res.state = "negative"
		else:
			res.state = None
		return res

	def __mul__(self, r):
		res = Real()
		res.value = str(self.value) + "*" + str(r.value)
		if res.value == "*":
			res.value = ""
		if (self.state == "positive" and r.state == "positive") or \
			(self.state == "negative" and r.state == "negative"):
			res.state = "positive"
		elif (self.state == "positive" and r.state == "negative") or \
			(self.state == "positive" and r.state == "negative"):
			res.state = "negative"
		else:
			res.state = None
		return res

	def view(self):
		print(self.value)
		return self.value

	def eval(self):
		try:
			self.value = eval(self.value)
			self.evaluated = True
		except ValueError:
			self.evaluated = False
		return self

	def isPositive(self):
		self.state == "positive"

a1 = Real(state = "positive")
a2 = Real(state = "positive")
(a1 + a2).view()
print((a1 + a2).state)

import unittest
class TestStringMethods(unittest.TestCase):
    def test_Real(self):
		x = Real(3)
		y = Real(5)
		z = (x + y)
		self.assertEqual(z.view(), '3+5')
		self.assertEqual(z.eval().view(), 8)
		x = Real('a')
		y = Real('b')
		z = (x + y).view()
		self.assertEqual(z, 'a+b')

if __name__ == '__main__':
    unittest.main()
