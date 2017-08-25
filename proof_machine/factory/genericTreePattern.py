from pythonds.basic.queue import Queue

# Tree decomposition
# def safeGuardedTreeMapping(nodesCheckList, nodesList, treeMapCode, nodesDict):
# 	return genericTreeMapping(nodesList, treeMapCode, nodesDict)

def genericTreeMapping(nodesList, treeMapCode, nodesDict):
	targetNodesList = mapNodes(nodesList, nodesDict)
	resTree = baseThreeCodeToTree(treeMapCode)
	return relabelTree(resTree, targetNodesList)

# def genericTreeMapping(tree, treeMapCode, nodesDict, addNodesList = [], nodeTreeIndicator = [], pos = [], modifyList = []):
# 	nodesList = treeToNodes(tree, nodeTreeIndicator) + addNodesList
# 	nodesList = nodesTransform(nodesList, pos, modifyList)
# 	targetNodesList = mapNodes(nodesList, nodesDict)
# 	resTree = baseThreeCodeToTree(treeMapCode)
# 	return relabelTree(resTree, targetNodesList)

# This function maps a tree into a list of nodes/tree with breadth-first order
def treeToNodes(tree, nodeTreeIndicator = []):
	if nodeTreeIndicator == []:
		nodeTreeIndicator = '0' * numNodes(tree)
	# Node is 0, Tree is 1.
	res = [tree.getRootNode()]
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		nodeQueue.enqueue(L)
	if R != None:
		nodeQueue.enqueue(R)
	count = 1  #count must start at 1
	while not nodeQueue.isEmpty() and count < len(nodeTreeIndicator):
		current = nodeQueue.dequeue()
		if nodeTreeIndicator[count] == '0':
			res.append(current.getRootNode())
			L = current.getLeftChild()
			R = current.getRightChild()
			if L != None:
				nodeQueue.enqueue(L)
			if R != None:
				nodeQueue.enqueue(R)
		elif nodeTreeIndicator[count] == '1':
			res.append(current)
		count += 1
	return res	

# This function modifies a nodesList
# def nodesTransform(nodesList, pos, modifyList):
# 	if modifyList != []:
# 		for ind, node in enumerate(modifyList):
# 			nodesList[pos[ind] - 1] = node
# 	return nodesList

def mapNodes(nodesList, nodesDict):
	resList = []
	for ind, key in enumerate(nodesDict):
		resList.append(nodesList[nodesDict[key] - 1])  #must be in order
	return resList

# This function relabels the tree with a list of nodes with breadth-first order
def relabelTree(tree, nodeList):
	# Breadth-first relabelling
	head, tail = nodeList[0], nodeList[1:]
	if isinstance(head, BinaryTree):
		return head
	tree.setRootNode(head)
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		nodeQueue.enqueue(L)
	if R != None:
		nodeQueue.enqueue(R)
	while tail != []:
		head, tail = tail[0], tail[1:]
		current = nodeQueue.dequeue()
		if isinstance(head, Node):
			current.setRootNode(head)
			L = current.getLeftChild()
			R = current.getRightChild()
			if L != None:
				nodeQueue.enqueue(L)
			if R != None:
				nodeQueue.enqueue(R)
		elif isinstance(head, BinaryTree):
			current.setRootNode(head.getRootNode())
			current.setLeftChild(head.getLeftChild())
			current.setRightChild(head.getRightChild())
	return tree

# Helper function
# This function counts the number of nodes in a tree
def numNodes(tree):
	res = [tree.getRootNode()]
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		nodeQueue.enqueue(L)
	if R != None:
		nodeQueue.enqueue(R)
	while not nodeQueue.isEmpty():
		current = nodeQueue.dequeue()
		res.append(current.getRootNode())
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
		if R != None:
			nodeQueue.enqueue(R)
	return len(res)

# This function gets all sub-trees
def getAllParents(tree):
	numChildren = 0
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		nodeQueue.enqueue(tree.getLeftChild())
	if R != None:
		nodeQueue.enqueue(tree.getRightChild())
	res = [tree]
	while not nodeQueue.isEmpty():
		current = nodeQueue.dequeue()
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
		if R != None:
			nodeQueue.enqueue(R)
		if L != None or R != None:
			res.append(current)
	return res
