# Output function
def treeToString(tree):
        sVal = ""
        if tree.getRootNodeType() == 'function':
            return str(tree.getRootNodeValue()) + ' ' + treeToString(tree.getLeftChild())
        elif tree.getRootNodeType() == 'symbol':
            return str(tree.getRootNodeValue())
        elif tree.getRootNodeType() == 'operator':
            return '( ' + treeToString(tree.getLeftChild()) + ' ' + str(tree.getRootNodeValue()) + ' ' + treeToString(tree.getRightChild())+ ' )'
        # elif tree.getRootNode().getType() == 'parentheses':
            # return '( ' + treeToString(tree.getLeftChild()) + ' )'


def printFullTree(tree):
	print(tree.getRootNode().getValue())
	if tree.getLeftChild() != None:
		printFullTree(tree.getLeftChild())
	if tree.getRightChild() != None:
		printFullTree(tree.getRightChild())


# Tree operations
def add_x(tree, x):
	res = BinaryTree(Node("+", "operator"))
	res.insertLeft(tree)
	res.insertRight(x)
	return res

def x_add(tree, x):
	res = BinaryTree(Node("+", "operator"))
	res.insertLeft(x)
	res.insertRight(tree)
	return res

def div_x(tree, x):
	res = BinaryTree(Node("/", "operator"))
	res.insertLeft(tree)
	res.insertRight(x)
	return res


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
	parentOp = tree.getRootNodeValue()
	if parentOp == 'E' and tree.getLeftChildValue() == 'I':
		res = BinaryTree(Node("P", "function"))
		res.insertLeft(tree.getLeftChild().getLeftChild())
		return res
	return tree


# Linear operator: Matrix norm, Expectation, (homomorphism?)

# Expectation
def takeExpectation(tree):
	res = BinaryTree(Node("E", "function"))
	res.insertLeft(tree)
	return res


def pushInExpectation(tree, variableState):
	parentOp = tree.getRootNodeValue()
	if parentOp != "E":
		return tree
	
	subTree = tree.getLeftChild()
	op = subTree.getRootNodeValue()
	if op == '+':
		resTree = BinaryTree(Node('+', 'operator'))
		resTree.insertLeft(takeExpectation(subTree.getLeftChild()))
		resTree.insertRight(takeExpectation(subTree.getRightChild()))
	elif op == '*':
		l = subTree.getLeftChildValue()
		r = subTree.getRightChildValue()
		if isState(l, 'constant', variableState) or isState(r, 'constant', variableState):
			resTree = BinaryTree(Node('*', 'operator'))
			if isState(l, 'constant', variableState):
				resTree.insertLeft(takeExpectation(subTree.getLeftChild()))
			else:
				resTree.insertLeft(subTree.getLeftChild())
			if isState(r, 'constant', variableState):
				resTree.insertRight(takeExpectation(subTree.getRightChild()))
			else:
				resTree.insertRight(subTree.getRightChild())
	return resTree


def isState(sym, state, variableState):
	return state in variableState[sym]


def pullOutExpectation(tree, variableState):
	if tree.getLeftChildValue() != 'E' or tree.getRightChildValue() != 'E':
		return tree
	
	parentOp = tree.getRootNodeValue()
	leftTree = tree.getLeftChild()
	rightTree = tree.getRightChild()
	
	if parentOp == '+':
		resTree = BinaryTree(Node('+', 'operator'))
		resTree.insertLeft(leftTree.getLeftChild())
		resTree.insertRight(rightTree.getLeftChild())
		return takeExpectation(resTree)
	elif parentOp == '*':
		l = leftTree.getLeftChildValue()
		r = rightTree.getLeftChildValue()
		if isState(l, 'constant', variableState) and isState(r, 'constant', variableState):
			resTree = BinaryTree(Node('*', 'operator'))
			resTree.insertLeft(leftTree.getLeftChild())
			resTree.insertRight(rightTree.getLeftChild())
			return takeExpectation(resTree)
	return tree
