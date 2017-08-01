# Exponential function
def pushInExp(tree):
	#e^(a+b) = e^a * e^b
	if tree.getRootNodeValue() == 'exp':
		parentOp = tree.getLeftChild().getRootNodeValue()
		if parentOp == '+':
			targetLayer1Node = Node('*', 'operator')
			targetLayer2Node = Node('exp', 'function')
		elif parentOp == '-':
			targetLayer1Node = Node('/', 'operator')
			targetLayer2Node = Node('exp', 'function')
		else:
			return tree
		return oneOneVerticalToOneTwoVertical(tree, targetLayer1Node, targetLayer2Node)
	return tree

def pullOutExp(tree):
	#e^a * e^b = e^(a+b)
	parentOp = tree.getRootNodeValue()
	if tree.getLeftChildValue() == 'exp' and tree.getLeftChildValue() == tree.getRightChildValue():
		if parentOp == '*':
			targetLayer1Node = Node('exp', 'function')
			targetLayer2Node = Node('+', 'operator')
		elif parentOp == '/':
			targetLayer1Node = Node('exp', 'function')
			targetLayer2Node = Node('-', 'operator')
		else:
			return tree
		return oneTwoVerticalToOneOneVertical(tree, targetLayer1Node, targetLayer2Node)
	return tree

# Logarithmic function
def pushInLog(tree):
	# log (ab) = log a + log b
	if tree.getRootNodeValue() == 'log':
		parentOp = tree.getLeftChild().getRootNodeValue()
		if parentOp == '*':
			targetLayer1Node = Node('+', 'operator')
			targetLayer2Node = Node('log', 'function')
		elif parentOp == '/':
			targetLayer1Node = Node('-', 'operator')
			targetLayer2Node = Node('log', 'function')
		else:
			return tree
		return oneOneVerticalToOneTwoVertical(tree, targetLayer1Node, targetLayer2Node)
	return tree

def pullOutLog(tree):
	# log a + log b = log (ab)
	parentOp = tree.getRootNodeValue()
	if tree.getLeftChildValue() == 'log' and tree.getLeftChildValue() == tree.getRightChildValue():
		if parentOp == '+':
			targetLayer1Node = Node('log', 'function')
			targetLayer2Node = Node('*', 'operator')
		elif parentOp == '-':
			targetLayer1Node = Node('log', 'function')
			targetLayer2Node = Node('/', 'operator')
		else:
			return tree
		return oneTwoVerticalToOneOneVertical(tree, targetLayer1Node, targetLayer2Node)
	else:
		return tree

# Associative law
def forwardAssociative(tree):
	#(a op1 b) op2 c = a op1 (b op2 c)
	associativeDict = {'++': '++', '+-': '+-', '-+': '--', '--': '-+', \
						'**': '**', '*/': '*/', '/*' : '//', '//': '/*', '^^': '^^'}
	op1 = tree.getLeftChildValue()
	op2 = tree.getRootNodeValue()
	if op1 + op2 in associativeDict:
		newop1, newop2 = associativeDict[op1 + op2]
		return twoOneHorizontalToOneTwoHorizontal(tree, Node(newop1, 'operator'), Node(newop2, 'operator'))
	return tree

def backwardAssociative(tree):
	#(a op1 b) op2 c = a op1 (b op2 c)
	associativeDict = {'++': '++', '+-': '+-', '-+': '--', '--': '-+', \
						'**': '**', '*/': '*/', '/*' : '//', '//': '/*', '^^': '^^'}
	op1 = tree.getRootNodeValue()
	op2 = tree.getRightChildValue()
	if op1 + op2 in associativeDict:
		newop1, newop2 = associativeDict[op1 + op2]
		return oneTwoHorizontalToTwoOneHorizontal(tree, Node(newop1, 'operator'), Node(newop2, 'operator'))
	return tree


# Linearity 
def distributive(tree, fun):
	# fun(X + Y) = fun(X) + fun(Y)
	subtree = tree.getLeftChild()
	if subtree.getRootNodeValue() == '+':
		X = subtree.getLeftChild()
		Y = subtree.getRightChild()
		res = BinaryTree(Node('+', 'operator'))
		res.insertLeft(ApplyFunctionToTree(X, fun))
		res.insertRight(ApplyFunctionToTree(Y, fun))
	return res

def factorise(tree):
	# fun(X) + fun(Y) = fun(X + Y)
	if tree.getRootNodeValue() == '+':
		if tree.getLeftChildValue() == tree.getRightChildValue():
			fun = tree.getLeftChildValue()
			X = tree.getLeftChild().getLeftChild()
			Y = tree.getRightChild().getLeftChild()
			res = BinaryTree(Node('+', 'operator'))
			res.insertLeft(X)
			res.insertRight(Y)
			res = ApplyFunctionToTree(res, fun)
	return res
			

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

