def addOneNodeOnTop(tree, node):
	res = BinaryTree(node)
	res.insertLeft(tree)
	return res

def twoVerticalNodesToOneNode(tree, node):
	res = BinaryTree(node)
	res.insertLeft(tree.getLeftChild().getLeftChild())
	return res

def oneNodeToTwoVerticalNodes(tree, node1, node2):
	res = tree.getLeftChild()
	res = addOneNodeOnTop(res, node2)
	res = addOneNodeOnTop(res, node1)
	return res
	
def oneOneVerticalToOneTwoVertical(tree, layer1Node, layer2Node):
	X = tree.getLeftChild().getLeftChild()
	Y = tree.getLeftChild().getRightChild()
	res = BinaryTree(layer1Node)
	res.insertLeft(addOneNodeOnTop(X, layer2Node))
	res.insertRight(addOneNodeOnTop(Y, layer2Node))
	return res

def oneTwoVerticalToOneOneVertical(tree, layer1Node, layer2Node):
	X = tree.getLeftChild().getLeftChild()
	Y = tree.getRightChild().getLeftChild()
	res = BinaryTree(layer2Node)
	res.insertLeft(X)
	res.insertRight(Y)
	res = addOneNodeOnTop(res, layer1Node)
	return res

def twoOneHorizontalToOneTwoHorizontal(tree, node1, node2):
	# node1 refers to the first layer, node2 refers to the second layer
	X = tree.getLeftChild().getLeftChild()
	Y = tree.getLeftChild().getRightChild()
	Z = tree.getRightChild()
	res = BinaryTree(node1)
	res.insertLeft(X)
	subres = BinaryTree(node2)
	subres.insertLeft(Y)
	subres.insertRight(Z)
	res.insertRight(subres)
	return res

def oneTwoHorizontalToTwoOneHorizontal(tree, node1, node2):
	X = tree.getLeftChild()
	Y = tree.getRightChild().getLeftChild()
	Z = tree.getRightChild().getRightChild()
	res = BinaryTree(node1)
	res.insertRight(Z)
	subres = BinaryTree(node2)
	subres.insertLeft(X)
	subres.insertRight(Y)
	res.insertLeft(subres)
	return res
