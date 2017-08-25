class IntervalList:
	def __init__(self):
		self.list = []
		
class Interval:
	def __init__(self, myInterval):
		myInterval = sorted(myInterval)
		self.left = myInterval[0]
		self.right = myInterval[1]

	def length(self):
		self.right - self.left

	def supUnion(self, myInterval):
		res = Interval([self.left, self.right])
		res.left = "min(" + str(res.left) + "," + str(myInterval.left) + ")"
		res.right = "max(" + str(res.right) + "," + str(myInterval.right) + ")"
		return res

	def intersection(self, myInterval):
		res = Interval([self.left, self.right])
		res.left = "max(" + str(res.left) + "," + str(myInterval.left) + ")"
		res.right = "min(" + str(res.right) + "," + str(myInterval.right) + ")"
		return res

	def isOverlap(self, myInterval):
		self.intersection
		
	def isEmpty(self):
		self.left == None and self.right == None

	def view(self):
		print([self.left, self.right])
		return([self.left, self.right])

	def eval(self):
		try:
			self.left = eval(self.left)
			self.right = eval(self.right)
			self.evaluated = True
			if self.right < self.left:
				self.left = None
				self.right = None
		except ValueError:
			self.evaluated = False
		return self


import unittest
class TestStringMethods(unittest.TestCase):
    def test_Interval(self):
		x = Interval([3, 4])
		y = Interval([1, 2])
		self.assertEqual(x.supUnion(y).view(), ['min(3,1)', 'max(4,2)'])
		self.assertEqual(x.supUnion(y).eval().view(), [1,4])
		self.assertEqual(x.intersection(y).view(), ['max(3,1)', 'min(4,2)'])
		self.assertEqual(x.intersection(y).eval().view(), [None, None])

if __name__ == '__main__':
    unittest.main()
