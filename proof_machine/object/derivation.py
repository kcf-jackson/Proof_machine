from proof_machine.objClass.classTree import BinaryTree
from proof_machine.treeMap.treeParser import parse, tidyView

class Derivation:
	# The Derivation class is a list of tree expression
	def __init__(self, tree, namespace):
		self.exprList = [tree]
		self.namespace = namespace

	def View(self):
		for ind, tree in enumerate(self.exprList):
			if ind == 0:
				# tree.View()
				tidyView(tree, self.namespace)
			else:
				# print('= ' + treeToString(tree))
				print('= ' + tidyView(tree, self.namespace, False))

	# Basic operations
	def derive(self, fun):
		if len(self.exprList) != 0:
			self.exprList.append(fun(self.exprList[-1]))

	# this function takes the last expression, replaces a specified substring / subtree by its transform
	def substitute(self, subTree, fun):
		if not isinstance(subTree, BinaryTree):
			subTree = parse(subTree, self.namespace)
		if len(self.exprList) != 0:
			self.exprList.append(substitute(self.exprList[-1], subTree, fun(subTree), self.namespace))

	# this function takes the last expression, replaces a specified substring / subtree by a substring / subtree
	def replace(self, subTree, newTree):
		if not isinstance(subTree, BinaryTree):
			subTree = parse(subTree, self.namespace)
		if not isinstance(newTree, BinaryTree):
			newTree = parse(newTree, self.namespace)
		if len(self.exprList) != 0:
			self.exprList.append(substitute(self.exprList[-1], subTree, newTree, self.namespace))

	def removeDuplication(self):
		self.exprList = removeDuplication(self.exprList, self.namespace)

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
			newList = removeDuplication(deriveNewExpr(current, funList, self.namespace, quiet), self.namespace)
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
			newList = removeDuplication(deriveNewExpr(current, funList, self.namespace, quiet), self.namespace)
			self.exprList.append(minDiffTree(targetTree, newList))
			if treeDiff(self.exprList[-1], targetTree) == 0:
				break
		print("Difference score of the final expression and the target expression: " + str(treeDiff(self.exprList[-1], targetTree)))

def autoDeriveBreadth(deriveObj, funList, namespace, steps = 5, quiet = True):
	fullList = [ [0, deriveObj.exprList[-1]] ]
	for i in range(steps):
		S = subsetByLayer(fullList, i)
		for exprWithMeta in S:
			expr = exprWithMeta[1]
			newList = removeDuplication(deriveNewExpr(expr, funList, namespace, quiet), namespace)
			fullList += appendIndexToExpr(newList, i + 1)
	return fullList			

def deriveNewExpr(tree, funList, namespace, quiet = True):
	# given a tree and a list of functions, apply each function to all subtrees (when possible)
	# return the list of new expressions
	treeList = getAllParents(tree)
	resList = []
	for subTree in treeList:
		for ind, fun in enumerate(funList):
			transformedTree = fun(subTree)
			if transformedTree != subTree:
				resList.append(substitute(tree, subTree, transformedTree, namespace))
				if not quiet:
					print(treeToString(subTree) + ' -> ' + treeToString(transformedTree))
	return resList

# Helper functions
def subsetByLayer(fullList, i):
	return [item for item in fullList if item[0] == i]

def appendIndexToExpr(exprList, i):
	return [[i, item] for item in exprList]

def removeDuplication(treeList, namespace):
	strList = [treeToString(tree) for tree in treeList]
	return [parse(x, namespace) for x in unique(strList)]

def substitute(originTree, oldTree, newTree, namespace):
	# return parse(treeToString(originTree).replace(treeToString(oldTree), treeToString(newTree)), namespace)
	return parse(treeToString(originTree).replace(treeToString(oldTree), treeToString(newTree)), namespace)
