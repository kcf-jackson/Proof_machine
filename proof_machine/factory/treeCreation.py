from pythonds.basic.queue import Queue

# Convert LR code to baseThreeCode
def LRcodeToBaseThreeCode(LRcode):
	if LRcode == [] or len(LRcode) == 0:
		return '0'
	paths = [x for x in LRcode.split('0') if x != '']
	maxPathLength = max(map(len, paths))
	children = ['L', 'R']
	res = ""
	for i in range(maxPathLength + 1):
		head = unique([x[:(i+1)] for x in paths])
		newCompletePath, head = [x for x in head if len(x) == i], [x for x in head if len(x) >= (i+1)]
		if newCompletePath != []:
			res += '0' * len(newCompletePath)
		for ind, item in enumerate(children):
			if ind % 2 == 1:
				hasChildren = [x in head for x in children[(ind - 1):(ind + 1)]]
				numChildren = sum(hasChildren)
				if numChildren != 0:
					res += str(numChildren)
		children = sum([[x+'L', x+'R'] for x in children], [])
	return res 

def unique(list0):
	return list(set(list0))

# Convert baseThreeCode to LR code
def baseThreeCodeToLRcode(baseThreeCode):
	i, baseThreeCode = baseThreeCode[0], baseThreeCode[1:]
	if i in ['0', '1', '2']:
		path = ['L','R'][:int(i)]
	else: 
		throw("The following character is not allowed: " + i + ", use only one of '0', '1', '2'.") 
	completedPath = []
	while path != [] and baseThreeCode != '':
		n = numOpenPath(path)
		i, baseThreeCode = baseThreeCode[:n], baseThreeCode[n:]
		allPaths = map2(path, i, addLRString)
		completedPath.append([x for x in allPaths if isPathEnd(x)])
		path = [x for x in allPaths if not isPathEnd(x)]
	return "".join(sum(completedPath, []))

def map2(list1, list2, FUN):
	res = []
	for ind, i in enumerate(list1):
		res.append(FUN(list1[ind], list2[ind]))
	return sum(res, [])

def isPathEnd(str0):
	return str0[-1] == '0'

def numOpenPath(list0):
	return len(list0) - sum(map(isPathEnd, list0))

def addLRString(str0, i):
	i = str(i)
	localDict = {'0': [str0 + '0'], '1': [str0 + 'L'], '2': [str0 + 'L', str0 + 'R']}
	if i in ['0', '1', '2']:
		return localDict[i]
	else:
		throw("Error occurs in addLRString, input was " + str0 + ", " + i)

# Build tree from LR / baseThree(B3) code
# [Export]
def LRcodeToTree(LRcode):
	masterTree = BinaryTree(Node('root', 'symbol'))
	workingTree = masterTree
	for i in LRcode:
		if i == '0':
			workingTree = masterTree
		elif i == 'L':
			if workingTree.getLeftChild() == None:
				workingTree.insertLeft(Node('L', 'symbol'))
			workingTree = workingTree.getLeftChild()
		elif i == 'R':
			if workingTree.getRightChild() == None:
				workingTree.insertRight(Node('R', 'symbol'))
			workingTree = workingTree.getRightChild()
		else:
			print("Character " + i + " is not allowed.")
	return masterTree

# [Export]
def baseThreeCodeToTree(baseThreeCode):
	return LRcodeToTree(baseThreeCodeToLRcode(baseThreeCode))

# Tree decomposition
# [Export]
def genericTreeMapping(tree, treeMapCode, nodesDict, addNodesList = [], nodeTreeIndicator = []):
	nodesList = treeToNodes(tree, nodeTreeIndicator) + addNodesList
	targetNodesList = mapNodes(nodesList, nodesDict)
	resTree = baseThreeCodeToTree(treeMapCode)
	return relabelTree(resTree, targetNodesList)

# This function maps a tree into a list of nodes/tree with breadth-first order
def treeToNodes(tree, nodeTreeIndicator = []):
	if nodeTreeIndicator == []:
		nodeTreeIndicator = '0' * numNodes(tree)
	# Node is 0, Tree is 1.
	res = [tree.getRootNode()]
	nodeQueue = Queue()
	nodeQueue.enqueue(tree.getLeftChild())
	nodeQueue.enqueue(tree.getRightChild())
	count = 0
	while not nodeQueue.isEmpty():
		current = nodeQueue.dequeue()
		if nodeTreeIndicator[count] == '0':
			res.append(current.getRootNode())
		elif nodeTreeIndicator[count] == '1':
			res.append(current)
		count += 1
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
		if R != None:
			nodeQueue.enqueue(R)
	return res	

# This function counts the number of nodes in a tree
def numNodes(tree):
	res = [tree.getRootNode()]
	nodeQueue = Queue()
	nodeQueue.enqueue(tree.getLeftChild())
	nodeQueue.enqueue(tree.getRightChild())
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

def mapNodes(nodesList, nodesDict):
	resList = []
	for i in range(len(nodesDict)):
		resList.append(nodesList[nodesDict[i + 1] - 1])  #must be in order
	return resList

# This function relabels the tree with a list of nodes with breadth-first order
def relabelTree(tree, nodeList):
	# Breadth-first relabelling
	head, tail = nodeList[0], nodeList[1:]
	tree.setRootNode(head)
	nodeQueue = Queue()
	nodeQueue.enqueue(tree.getLeftChild())
	nodeQueue.enqueue(tree.getRightChild())
	while tail != []:
		head, tail = tail[0], tail[1:]
		current = nodeQueue.dequeue()
		# if isinstance(head, Node):
		current.setRootNode(head)
		# elif isinstance(head, BinaryTree):
			# current = head
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
		if R != None:
			nodeQueue.enqueue(R)
	return tree
