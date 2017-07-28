def getClass(obj):
	return obj.__class__.__name__

class Undefined():
	def __init__(self):
		self.value = "Undefined"
		self.negation = "Undefined"
	def __add__(self, r):
		return self
	def __sub__(self, r):
		return self
	def __mul__(self, r):
		return self
	def __div__(self, r):
		return self
	def __pow__(self, r):
		return self
	def __radd__(self, l):
		return self
	def __rsub__(self, l):
		return self
	def __rmul__(self, l):
		return self
	def __rdiv__(self, l):
		return self
	def __rpow__(self, l):
		return self
	def __neg__(self):
		return self
	def reciprocal(self):
		return self
	def view(self):
		return "Undefined"

class Infinity():
	def __init__(self):
		self.value = "Inf"
		self.negation = False

	def copy(self):
		b = Infinity()
		b.value = self.value
		b.negation = self.negation
		return b

	def undefined(self):
		a = Undefined()
		return a

	def __add__(self, r):
		b = self.copy()
		if getClass(r) == 'Undefined':
			return r
		elif getClass(r) == 'Infinity':
			if b.negation != r.negation:
				return b.undefined()
		return b
	
	def __radd__(self, l):
		return self.__add__(l)

	def __sub__(self, r):
		r = -r
		return self.__add__(r)
	
	def __rsub__(self, l):
		self = -self
		return self.__radd__(l)

	def __mul__(self, r):
		b = self.copy()
		if getClass(r) == 'Undefined':
			return r
		elif getClass(r) == 'Infinity':
			b.negation = (self.negation != r.negation)
		elif getClass(r) in ['int', 'float']:
			if r == 0:
				return b.undefined()
			elif r < 0:
				b.negation = not b.negation 
		return b

	def __rmul__(self, l):
		return self.__mul__(l)
	
	def __div__(self, r):
		if getClass(r) == 'Infinity':
			r = r.reciprocal()
		elif getClass(r) in ['int', 'float']:
			if r == 0:
				r = Infinity()
		return self.__mul__(r)

	def __rdiv__(self, l):
		return l * 0
		
	def __neg__(self):
		b = self.copy()
		b.negation = not b.negation
		return b

	def reciprocal(self):
		return 0

	def __pow__(self, r):
		b = self.copy()
		if not b.negation:
			if (getClass(r) == "Infinity"):
				if r.negation:
					return 0
				else:
					return b
			elif (getClass(r) in ['int', 'float']):
				if r > 0:
					return b
				elif r == 0:
					return 1
				elif r < 0:
					return 0
			return Undefined()
		else:
			if (getClass(r) == "Infinity"):
				return Undefined()
			elif (getClass(r) in ['int', 'float']):
				if r > 0:
					return b
				elif r == 0:
					return 1
				elif r < 0:
					return 0
			return Undefined()

	def __rpow__(self, l):
		b = self.copy()
		if getClass(l) == "Infinity":
			return l.__pow__(self)
		elif getClass(l) in ['int', 'float']:
			if l > 0:
				if not b.negation:
					return Infinity()
				else:
					return 0
			elif l == 0:
				if not b.negation:
					return 0
				else:
					return Infinity()
			elif l < 0:
				return Undefined()
		return Undefined()

	def view(self):
		prefix = ''
		if self.negation:
			prefix = '-'
		return prefix + self.value

# import unittest
# class TestStringMethods(unittest.TestCase):
#     def test_Infinity(self):
# 		a = Infinity()
# 		a2 = -Infinity()
# 		b = 3
# 		c = 0
# 		d = -3
# 		e = Undefined()
# 		testCases = [a, a2, b, c, d, e]
# 		# Object initialisation
# 		print("-----Test initialisation-----")
# 		self.assertEqual(a.view(), "Inf")
		
# 		# Negation
# 		print("\n-----Test negation-----")
# 		self.assertEqual((-a).view(), "-Inf")
# 		self.assertEqual(a.view(), "Inf")   # this check the object is not modified
		
# 		# Left addition
# 		print("\n-----Test left addition-----")
# 		ansList = ["Inf", "Undefined", "Inf", "Inf", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((a + case).view(), ansList[i])
# 		ansList = ["Undefined", "-Inf", "-Inf", "-Inf", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((-a + case).view(), ansList[i])

# 		# Right addition
# 		print("\n-----Test right addition-----")
# 		ansList = ["Inf", "Undefined", "Inf", "Inf", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((case + a).view(), ansList[i])
# 		ansList = ["Undefined", "-Inf", "-Inf", "-Inf", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((case + -a).view(), ansList[i])

# 		# Left subtraction
# 		print("\n-----Test left subtraction-----")
# 		ansList = ["Undefined", "Inf", "Inf", "Inf", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((a - case).view(), ansList[i])
# 		ansList = ["-Inf", "Undefined", "-Inf", "-Inf", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((-a - case).view(), ansList[i])

# 		# Right subtraction
# 		print("\n-----Test right subtraction-----")
# 		ansList = ["Undefined", "Inf", "Inf", "Inf", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((a - case).view(), ansList[i])
# 		ansList = ["-Inf", "Undefined", "-Inf", "-Inf", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((-a - case).view(), ansList[i])

# 		# Reciprocal
# 		print("\n-----Test reciprocal-----")
# 		self.assertEqual((-a).reciprocal(), 0)
# 		self.assertEqual(a.reciprocal(), 0)   # this check the object is not modified
		
# 		# Left multiplication
# 		print("\n-----Test left multiplication-----")
# 		ansList = ["Inf", "-Inf", "Inf", "Undefined", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((a * case).view(), ansList[i])
# 		ansList = ["-Inf", "Inf", "-Inf", "Undefined", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual(((-a) * case).view(), ansList[i])

# 		# Right multiplication
# 		print("\n-----Test right multiplication-----")
# 		ansList = ["Inf", "-Inf", "Inf", "Undefined", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((case * a).view(), ansList[i])
# 		ansList = ["-Inf", "Inf", "-Inf", "Undefined", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((case * (-a)).view(), ansList[i])

# 		# Left division
# 		print("\n-----Test left division-----")
# 		ansList = ["Undefined", "Undefined", "Inf", "Inf", "-Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual((a / case).view(), ansList[i])
# 		ansList = ["Undefined", "Undefined", "-Inf", "-Inf", "Inf", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			self.assertEqual(((-a) / case).view(), ansList[i])

# 		# Right division
# 		print("\n-----Test right division-----")
# 		ansList = ["Undefined", "Undefined", 0, 0, 0, "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass(case) in ['int', 'float']:
# 				self.assertEqual((case / a), ansList[i])	
# 			else:
# 				self.assertEqual((case / a).view(), ansList[i])
# 		ansList = ["Undefined", "Undefined", 0, 0, 0, "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass(case) in ['int', 'float']:
# 				self.assertEqual((case / (-a)), ansList[i])
# 			else:
# 				self.assertEqual((case / (-a)).view(), ansList[i])
		
# 		# Left power
# 		print("\n-----Test left power-----")
# 		ansList = ["Inf", 0, "Inf", 1, 0, "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass(a ** case) in ['int', 'float']:
# 				self.assertEqual((a ** case), ansList[i])
# 			else:
# 				self.assertEqual((a ** case).view(), ansList[i])
# 		ansList = ["Undefined", "Undefined", "-Inf", 1, 0, "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass((-a) ** case) in ['int', 'float']:
# 				self.assertEqual((-a) ** case, ansList[i])
# 			else:
# 				self.assertEqual(((-a) ** case).view(), ansList[i])

# 		# Right power
# 		print("\n-----Test right power-----")
# 		ansList = ["Inf", "Undefined", "Inf", 0, "Undefined", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass(case ** a) in ['int', 'float']:
# 				self.assertEqual(case ** a, ansList[i])
# 			else:
# 				self.assertEqual((case  ** a).view(), ansList[i])
# 		ansList = [0, "Undefined", 0, "Inf", "Undefined", "Undefined"]
# 		for i, case in enumerate(testCases):
# 			if getClass(case ** (-a)) in ['int', 'float']:
# 				self.assertEqual(case ** (-a), ansList[i])
# 			else:
# 				self.assertEqual((case ** (-a)).view(), ansList[i])
			
# if __name__ == '__main__':
#     unittest.main()

# Unit test
# Setup
a = Infinity()
a2 = -Infinity()
b = 3
c = 0
d = -3
e = Undefined()

testCases = [a, a2, b, c, d, e]
testStr = ['a', 'a2', 'b', 'c', 'd', 'e']
printStr = ['Inf', '-Inf', '3', '0', '-3', 'NaN']
operations = ['+', '-', '*', '/', '**']
count = 1
for k, dk in enumerate(operations):
	for i, di in enumerate(testStr):
		for j, dj in enumerate(testStr):
			printExpr = printStr[i] + " " + operations[k] + " " + printStr[j]
			expr = testStr[i] + operations[k] + testStr[j]
			try:
				ans = eval(expr)
				if getClass(ans) in ['int', 'float']:
					print(str(count) + ": " + printExpr + " = " + str(eval(expr)))
				else:
					print(str(count) + ": " + printExpr + " = " + str(eval(expr).view()))
			except ZeroDivisionError:
				print(str(count) + ": Python does not handle division by zero.")
				count += 1
				continue
			count += 1
