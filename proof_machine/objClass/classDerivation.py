class Derivation:
	# The Derivation class is a list of tree expression
	def __init__(self, tree):
		self.exprList = [tree]

	def view(self):
		for ind, tree in enumerate(self.exprList):
			if ind == 0:
				tree.view()
			else:
				print('= ' + treeToString(tree))

	# Basic operations
	def derive(self, fun):
		if len(self.exprList) != 0:
			self.exprList.append(fun(self.exprList[-1]))

	def substitute(self, subTree, fun):
		if not isinstance(subTree, BinaryTree):
			subTree = parseTree(subTree)
		if len(self.exprList) != 0:
			self.exprList.append(substitute(self.exprList[-1], subTree, fun(subTree)))

	def replace(self, subTree, newTree):
		if not isinstance(subTree, BinaryTree):
			subTree = parseTree(subTree)
		if not isinstance(newTree, BinaryTree):
			newTree = parseTree(newTree)
		if len(self.exprList) != 0:
			self.exprList.append(substitute(self.exprList[-1], subTree, newTree))

	def removeDuplication(self):
		self.exprList = removeDuplication(self.exprList)

	# Automatic derivation
	def blindDerive(self, funList, steps = 5, quiet = True, randomized = True):
		import random
		for i in range(steps):
			treeList = getAllParents(self.exprList[-1])
			for subTree in treeList:
				l = len(funList)
				rind = random.sample(list(range(l)), l) if randomized else list(range(l))
				for ind in rind:
					fun = funList[ind]
					transformedTree = fun(subTree)
					if transformedTree != subTree:
						self.replace(subTree, transformedTree)
						if not quiet:
							print(treeToString(subTree) + ' -> ' + treeToString(transformedTree))
		self.removeDuplication()

	def semiAutoDerive(self, funList, quiet = True):
		current = self.exprList[-1]
		continueFlag = True
		while continueFlag:
			print("\n" + treeToString(current) + " = ")
			newList = removeDuplication(deriveNewExpr(current, funList, quiet))
			for ind, newExpr in enumerate(newList):
				print(str(ind+1) + ": " + treeToString(newExpr))
			choice = input("Which line do you want to continue with (Type 'q' to end)? ")
			if choice == 'q':
				continueFlag = False
				break
			elif 1 <= int(choice) <= len(newList):
				current = newList[int(choice) - 1]
				self.exprList.append(current)
			else:
				continue

	def autoDerive(self, targetTree, funList, steps = 5, quiet = True):
		for i in range(steps):
			current = self.exprList[-1]
			print(("" if i == 0 else "= ") + treeToString(current))
			newList = removeDuplication(deriveNewExpr(current, funList, quiet))
			self.exprList.append(minDiffTree(targetTree, newList))
			if treeDiff(self.exprList[-1], targetTree) == 0:
				break
		print("Difference score of the final expression and the target expression: " + str(treeDiff(self.exprList[-1], targetTree)))

def autoDeriveBreadth(deriveObj, funList, steps = 5, quiet = True):
	fullList = [ [0, deriveObj.exprList[-1]] ]
	for i in range(steps):
		S = subsetByLayer(fullList, i)
		for exprWithMeta in S:
			expr = exprWithMeta[1]
			newList = removeDuplication(deriveNewExpr(expr, funList, quiet))
			fullList += appendIndexToExpr(newList, i + 1)
	return fullList			

def deriveNewExpr(tree, funList, quiet = True):
	# given a tree and a list of functions, apply each function to all subtrees (when possible)
	# return the list of new expressions
	treeList = getAllParents(tree)
	resList = []
	for subTree in treeList:
		for ind, fun in enumerate(funList):
			transformedTree = fun(subTree)
			if transformedTree != subTree:
				resList.append(substitute(tree, subTree, transformedTree))
				if not quiet:
					print(treeToString(subTree) + ' -> ' + treeToString(transformedTree))
	return resList

# Helper functions
def subsetByLayer(fullList, i):
	return [item for item in fullList if item[0] == i]

def appendIndexToExpr(exprList, i):
	return [[i, item] for item in exprList]

def removeDuplication(treeList):
	strList = [treeToString(tree) for tree in treeList]
	return list(map(parseTree, unique(strList)))

def substitute(originTree, oldTree, newTree):
	return parseTree(treeToString(originTree).replace(treeToString(oldTree), treeToString(newTree)))
