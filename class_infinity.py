def getClass(obj):
	return obj.__class__.__name__

class Infinity():
	def __init__(self):
		self.value = "Inf"
		self.negation = False

	def undefined(self):
		self.value = "Undefined"
		self.negation = "Undefined"

	# need to take care of "Inf - Inf" for add and sub.
	def __add__(self, r):
		if getClass(r) == 'Infinity':
			if self.negation != r.negation:
				self.undefined()
		return self
	
	def __sub__(self, r):
		if getClass(r) == 'Infinity':
			if self.negation == r.negation:
				self.undefined()
		return self
	
	def __radd__(self, r):
		return self.__add__(r)

	def __rsub__(self, r):
		if getClass(r) == 'Infinity':
			if self.negation == r.negation:
				self.undefined()
		return -self

	# need to take care of "Inf / Inf" for add and sub.	
	# for real numbers, take care of the sign
	def __mul__(self, r):
		if getClass(r) == 'Infinity':
			self.negation = (self.negation == r.negation)
		elif getClass(r) in ['int', 'float']:
			if r == 0:
				self.undefined()
			elif r < 0:
				self.negation = not self.negation 
		return self

	def __rmul__(self, r):
		return self.__mul__(r)
	
	def __div__(self, r):
		if getClass(r) == 'Infinity':
			self.undefined()
		elif getClass(r) in ['int', 'float']:
			if r == 0:
				self.undefined()
			elif r < 0:
				self.negation = not self.negation 
		return self

	def __rdiv__(self, r):
		if getClass(r) == 'Infinity':
			self.undefined()
		elif getClass(r) in ['int', 'float']:
			if r == 0:
				self.undefined()
			elif r < 0:
				self.negation = not self.negation 
		return self

	def __neg__(self):
		self.negation = not self.negation
		return self

	# def __pow__(self, r):
		

	# def __rpow__(self, r):
	# 	self.


	def view(self):
		prefix = ''
		if self.negation:
			prefix = '-'
		print(prefix + self.value)


a = Infinity()
a2 = -Infinity()
b = 3
c = 0
d = -3

testCases = [a, a2, b, c, d]
for i in testCases:
	for j in testCases:
		(i + j).view()
		(i - j).view()
		(i * j).view()
		(i / j).view()