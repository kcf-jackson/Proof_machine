# Simplification
def simplifyPairs(tree, op1, op2):
	parentOp = tree.getRootNodeValue()
	if parentOp == op1 and tree.getLeftChildValue() == '*':
		subTree = tree.getLeftChild()
		if subTree.getLeftChildValue() == tree.getRightChildValue():
			return subTree.getRightChild()
		elif subTree.getRightChildValue() == tree.getRightChildValue():
			return subTree.getLeftChild()
	return tree

def simplifyPairsWithOrder(tree, op1, op2):
	parentOp = tree.getRootNodeValue()
	if parentOp == op1 and tree.getLeftChildValue() == '*':
		subTree = tree.getLeftChild()
		if subTree.getLeftChildValue() == tree.getRightChildValue():
			return subTree.getRightChild()
		elif subTree.getRightChildValue() == tree.getRightChildValue():
			return subTree.getLeftChild()
	return tree

def simplifyPairsWithState(tree, op1, op2):
	parentOp = tree.getRootNodeValue()
	if parentOp == op1 and tree.getLeftChildValue() == '*':
		subTree = tree.getLeftChild()
		if subTree.getLeftChildValue() == tree.getRightChildValue():
			return subTree.getRightChild()
		elif subTree.getRightChildValue() == tree.getRightChildValue():
			return subTree.getLeftChild()
	return tree

def simplifyPairsWithStateAndOrder(tree, op1, op2):
	parentOp = tree.getRootNodeValue()
	if parentOp == op1 and tree.getLeftChildValue() == '*':
		subTree = tree.getLeftChild()
		if subTree.getLeftChildValue() == tree.getRightChildValue():
			return subTree.getRightChild()
		elif subTree.getRightChildValue() == tree.getRightChildValue():
			return subTree.getLeftChild()
	return tree


def simplifyDiv(tree):
	parentOp = tree.getRootNodeValue()
	if parentOp == '/' and tree.getLeftChildValue() == '*':
		subTree = tree.getLeftChild()
		if subTree.getLeftChildValue() == tree.getRightChildValue():
			return subTree.getRightChild()
		elif subTree.getRightChildValue() == tree.getRightChildValue():
			return subTree.getLeftChild()
	return tree


def functionalToMeasure(tree):
	if tree.getRootNodeValue() == 'E' and tree.getLeftChildValue() == 'I':
		return twoVerticalNodesToOneNode(tree, Node('P', 'function'))
	return tree

def measureToFunctional(tree):
	if tree.getRootNodeValue() == 'P':
		return oneNodeToTwoVerticalNodes(tree, Node('E', 'function'), Node('I', 'function'))
	return tree
