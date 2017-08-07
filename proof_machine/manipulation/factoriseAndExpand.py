# Distributive law
def leftPushIn(tree):
	#(1,2,2) to (1,2,4) pattern
	# case 1: c*(a +/- b) = c*a +/- c*b
	# case 2: c^(a +/- b) = c^a *// c^b
	distOp = tree.getRootNodeValue()
	if distOp == '*':
		distributiveDict = {'+': '+', '-': '-'}
	if distOp == '^':
		distributiveDict = {'+': '*', '-': '/'}
	parentOp = tree.getRightChild().getRootNodeValue()
	if distOp + parentOp in ['*+', '*-', '^+', '^-']:
		a = tree.getRightChild().getLeftChild()
		b = tree.getRightChild().getRightChild()
		c = tree.getLeftChild()
		res = BinaryTree(Node(distributiveDict[parentOp], 'operator'))
		res.insertLeft(X_Operator_Tree(a, c, distOp))
		res.insertRight(X_Operator_Tree(b, c, distOp))
		return res
	return tree

def rightPushIn(tree):
	#(1,2,2) to (1,2,4) pattern
	# case 1: (a *// b) ^ c = a^c *// b^c
	# case 2: (a +/- b) * c = a*c +/- b*c
	# case 3: (a +/- b) / c = c*a +/- c*b
	distOp = tree.getRootNodeValue()
	if distOp in ['*', '/']:
		distributiveDict = {'+': '+', '-': '-'}
	if distOp == '^':
		distributiveDict = {'*': '*', '/': '/'}
	if distOp in ['cap', 'cup']:
		distributiveDict = {'cap': 'cap', 'cup': 'cup'}
	parentOp = tree.getLeftChild().getRootNodeValue()
	if distOp + parentOp in ['*+', '*-', '/+', '/-', '^*', '^/', 'capcup', 'cupcap']:
		a = tree.getLeftChild().getLeftChild()
		b = tree.getLeftChild().getRightChild()
		c = tree.getRightChild()		
		res = BinaryTree(Node(distributiveDict[parentOp], 'operator'))
		res.insertLeft(Tree_Operator_X(a, c, distOp))
		res.insertRight(Tree_Operator_X(b, c, distOp))
		return res
	return tree

def leftPullOut(tree):
	# c*a +/- c*b = c * (a +/- b)
	if tree.getRootNodeValue() in ['+', '-']:
		parentOp = tree.getLeftChildValue()
		if parentOp == '*' and tree.getLeftChildValue() == tree.getRightChildValue() and \
			tree.getLeftChild().getLeftChildValue() == tree.getRightChild().getLeftChildValue():
			a = tree.getLeftChild().getRightChild()
			b = tree.getRightChild().getRightChild()
			c = tree.getLeftChild().getLeftChild()
			res = BinaryTree(Node(parentOp, 'operator'))
			res.insertLeft(c)
			sub = BinaryTree(tree.getRootNode())
			sub.insertLeft(a)
			sub.insertRight(b)
			res.insertRight(sub)
			return res
	return tree

def rightPullOut(tree):
	# a * c +/- b * c = (a +/- b) * c
	# a / c +/- b / c = (a +/- b) / c
	if tree.getRootNodeValue() in ['+', '-']:
		parentOp = tree.getLeftChildValue()
		if parentOp in ['*', '/'] and tree.getLeftChildValue() == tree.getRightChildValue() and \
			tree.getLeftChild().getRightChildValue() == tree.getRightChild().getRightChildValue():
			a = tree.getLeftChild().getLeftChild()
			b = tree.getRightChild().getLeftChild()
			c = tree.getLeftChild().getRightChild()
			res = BinaryTree(Node(parentOp, 'operator'))
			res.insertRight(c)
			sub = BinaryTree(tree.getRootNode())
			sub.insertLeft(a)
			sub.insertRight(b)
			res.insertLeft(sub)
			return res
	return tree

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

# Linearity 
def functional_distribute(tree, funSym, variableState):
	# fun(X +/- Y) = fun(X) +/- fun(Y)
	# fun(a * X) = a * fun(X)
	subtree = tree.getLeftChild()
	parentOp = subtree.getRootNodeValue()
	if parentOp in ['+', '-']:
		X = subtree.getLeftChild()
		Y = subtree.getRightChild()
		res = BinaryTree(Node(parentOp, 'operator'))
		res.insertLeft(ApplyFunctionToTree(X, funSym))
		res.insertRight(ApplyFunctionToTree(Y, funSym))
		return res
	if parentOp in ['*', '/']:
		X = subtree.getLeftChild()
		Y = subtree.getRightChild()
		if isSymbol(X) or isSymbol(Y):
			if isConstant(X.getRootNodeValue(), variableState = variableState) or \
				isConstant(Y.getRootNodeValue(), variableState = variableState):
				res = BinaryTree(Node(parentOp, 'operator'))
				res.insertLeft(ApplyFunctionToTree(X, funSym))
				res.insertRight(ApplyFunctionToTree(Y, funSym))
				return res
	return tree

def functional_factorise(tree, variableState):
	# fun(X) +/- fun(Y) = fun(X +/- Y)
	# a * fun(X) = fun(a * X)
	parentOp = tree.getRootNodeValue()
	if parentOp in ['+', '-']:
		if tree.getLeftChildValue() == tree.getRightChildValue():
			funSym = tree.getLeftChildValue()
			X = tree.getLeftChild().getLeftChild()
			Y = tree.getRightChild().getLeftChild()
			res = BinaryTree(Node(parentOp, 'operator'))
			res.insertLeft(X)
			res.insertRight(Y)
			res = ApplyFunctionToTree(res, funSym)
			return res
	if parentOp in ['*', '/']:
		if tree.getLeftChildValue() == tree.getRightChildValue():
			funSym = tree.getLeftChildValue()
			X = tree.getLeftChild().getLeftChild()
			Y = tree.getRightChild().getLeftChild()
			if isSymbol(X) or isSymbol(Y):
				if isConstant(X.getRootNodeValue(), variableState = variableState) or \
					isConstant(Y.getRootNodeValue(), variableState = variableState):
					res = BinaryTree(Node(parentOp, 'operator'))
					res.insertLeft(X)
					res.insertRight(Y)
					res = ApplyFunctionToTree(res, funSym)
					return res
	return tree
			
# ========== To-do ==========
# pushInExpectation = partial(functional_distribute, funSym = "E", variableState = variableState)
# pullOutExpectation = partial(functional_distribute, variableState = variableState)

# def pullOutExpectation(tree, variableState):
# 	if tree.getLeftChildValue() != 'E' or tree.getRightChildValue() != 'E':
# 		return tree
	
# 	parentOp = tree.getRootNodeValue()
# 	leftTree = tree.getLeftChild()
# 	rightTree = tree.getRightChild()
	
# 	if parentOp == '+':
# 		resTree = BinaryTree(Node('+', 'operator'))
# 		resTree.insertLeft(leftTree.getLeftChild())
# 		resTree.insertRight(rightTree.getLeftChild())
# 		return takeExpectation(resTree)
# 	elif parentOp == '*':
# 		l = leftTree.getLeftChildValue()
# 		r = rightTree.getLeftChildValue()
# 		if isState(l, 'constant', variableState) and isState(r, 'constant', variableState):
# 			resTree = BinaryTree(Node('*', 'operator'))
# 			resTree.insertLeft(leftTree.getLeftChild())
# 			resTree.insertRight(rightTree.getLeftChild())
# 			return takeExpectation(resTree)
# 	return tree

# def pushInExpectation(tree, variableState):
# 	parentOp = tree.getRootNodeValue()
# 	if parentOp != "E":
# 		return tree
	
# 	subTree = tree.getLeftChild()
# 	op = subTree.getRootNodeValue()
# 	if op == '+':
# 		resTree = BinaryTree(Node('+', 'operator'))
# 		resTree.insertLeft(takeExpectation(subTree.getLeftChild()))
# 		resTree.insertRight(takeExpectation(subTree.getRightChild()))
# 	elif op == '*':
# 		l = subTree.getLeftChildValue()
# 		r = subTree.getRightChildValue()
# 		if isState(l, 'constant', variableState) or isState(r, 'constant', variableState):
# 			resTree = BinaryTree(Node('*', 'operator'))
# 			if isState(l, 'constant', variableState):
# 				resTree.insertLeft(takeExpectation(subTree.getLeftChild()))
# 			else:
# 				resTree.insertLeft(subTree.getLeftChild())
# 			if isState(r, 'constant', variableState):
# 				resTree.insertRight(takeExpectation(subTree.getRightChild()))
# 			else:
# 				resTree.insertRight(subTree.getRightChild())
# 	return resTree
