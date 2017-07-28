class Interval():
	# Single interval
	def __init__(self, myInterval):
		self.left = myInterval[0]
		self.right = myInterval[1]

	def supUnion(self, myInterval):


	def intersection(self, myInterval):
		if (self.)

	def add(self, myInterval):
		res = Interval()
		if self.left == 'Inf'
		res.left = self.left + myInterval.left
		res.right = self.right + myInterval.right
		return res

	def subtract(self, myInterval):
		res = Interval()
		res.left = self.left - myInterval.left
		res.right = self.right - myInterval.right
		return res

	def multiply(self, myInterval):
		res = Interval()
		combn = [self.left*myInterval.left, self.left*myInterval.right, \
					self.right*myInterval.left, self.right*myInterval.right]
		res.left = min(combn) 
		res.right = max(combn)
		return res

	def reciprocal(self):
		res = Interval()
		res.left = 1 / self.left
		res.right = 1 / self.right
		return res

	def divide(self, myInterval):
		res = Interval()
		return self.multiply(myInterval.reciprocal().left)
		

class UnionOfIntervals()
	self.interval = []
	self.openClose = []
	self.numDisjoint = []
