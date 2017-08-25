# Inclusion-exclusion formula
def inclusion_exclusion(tree):
	# assume tree is of form I - cup - A, B
	if tree.getRootNodeValue() == 'I' and tree.getLeftChildValue() == 'cup':
		I = tree.getRootNode()
		A = tree.getLeftChild().getLeftChild()
		B = tree.getLeftChild().getRightChild()
		res = BinaryTree(Node('-', 'operator'))

		leftTree = BinaryTree(Node('+', 'operator'))
		leftTree.insertLeft(addOneNodeOnTop(A, I))
		leftTree.insertRight(addOneNodeOnTop(B, I))

		rightTree = BinaryTree(Node('cap', 'operator'))
		rightTree.insertLeft(A)
		rightTree.insertRight(B)
		rightTree = addOneNodeOnTop(rightTree, I)

		res.insertLeft(leftTree)
		res.insertRight(rightTree)
		return res
	return tree

# Upper bound for indicator functions
def indicatorSumUpperBound(tree):
	if tree.getRootNodeValue() == 'I' and tree.getLeftChildValue() == 'cup_i':
		I = tree.getRootNode()
		A = tree.getLeftChild().getLeftChild()
		Sigma = Node('sum_i', 'function')
		return addNodesOnTop(A, [I, Sigma])
	return tree
