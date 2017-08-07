def invariant(tree):
	op = tree.getRootNodeValue()
	if tree.getLeftChildValue() == tree.getRightChildValue():
		if op in ['cap', 'cup']:
			return tree.getLeftChild()
	return tree

def symmetric(tree):
	op = tree.getRootNodeValue()
	if op in ['cap', 'cup', '*', '+', ]:
		resTree = BinaryTree(tree.getRootNode())
		resTree.leftChild, resTree.rightChild = tree.rightChild, tree.leftChild
		return resTree
	return tree
