class Derivation:
	# The Equation class has trees on both sides and an operator in-between.
	def __init__(self, tree):
		self.exprList = [tree]

	def view(self):
		for ind, tree in enumerate(self.exprList):
			if ind == 0:
				tree.view()
			else:
				print('= ' + treeToString(tree))

	def derive(self, fun):
		if len(self.exprList) != 0:
			self.exprList.append(fun(self.exprList[-1]))

	def substitute(self, subTree, fun):
		if len(self.exprList) != 0:
			self.exprList.append(substitute(self.exprList[-1], subTree, fun(subTree)))

def substitute(originTree, oldTree, newTree):
	return parseTree(treeToString(originTree).replace(treeToString(oldTree), treeToString(newTree)))
