def invariant(tree):
	op = tree.getRootNodeValue()
	if tree.getLeftChild() != None and tree.getRightChild() != None:
		if tree.getLeftChildValue() == tree.getRightChildValue():
			if op in ['cap', 'cup']:
				return tree.getLeftChild()
	return tree

def symmetry(tree):
	op = tree.getRootNodeValue()
	if op in ['cap', 'cup', '*', '+']:
		resTree = BinaryTree(tree.getRootNode())
		resTree.leftChild, resTree.rightChild = tree.rightChild, tree.leftChild
		return resTree
	return tree

def tautology(tree, op1, op2, sym):
	# example: tautology(tree, '+', '-', 'a') returns tree + a - a
	symNode = Node(sym, 'symbol')
	tree = addTopRight(tree, Node(op1, 'operator'), symNode)
	tree = addTopRight(tree, Node(op2, 'operator'), symNode)
	return tree
