from pythonds.basic.queue import Queue
from proof_machine.others import map2
from proof_machine.objClass import BinaryTree, Node

# Conversion between LR/baseThreeCode
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

# Build tree 
# Build from LR code
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

# Build from baseThree(B3) code
def baseThreeCodeToTree(baseThreeCode):
	return LRcodeToTree(baseThreeCodeToLRcode(baseThreeCode))

# Conversion from trees to codes
# Convert tree to baseThree code
def treeToBaseThreeCode(tree):
	numChildren = 0
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		numChildren += 1
		nodeQueue.enqueue(tree.getLeftChild())
	if R != None:
		numChildren += 1
		nodeQueue.enqueue(tree.getRightChild())
	res = [str(numChildren)]
	while not nodeQueue.isEmpty():
		current = nodeQueue.dequeue()
		numChildren = 0
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
			numChildren += 1
		if R != None:
			nodeQueue.enqueue(R)
			numChildren += 1
		res.append(str(numChildren))
	return "".join(res)

# Convert tree to leaves code
def treeToLeavesCode(tree):
	# Leaves are 1, others are 0
	numChildren = 0
	nodeQueue = Queue()
	L = tree.getLeftChild()
	R = tree.getRightChild()
	if L != None:
		numChildren += 1
		nodeQueue.enqueue(tree.getLeftChild())
	if R != None:
		numChildren += 1
		nodeQueue.enqueue(tree.getRightChild())
	res = '1' if numChildren == 0 else '0'
	while not nodeQueue.isEmpty():
		current = nodeQueue.dequeue()
		numChildren = 0
		L = current.getLeftChild()
		R = current.getRightChild()
		if L != None:
			nodeQueue.enqueue(L)
			numChildren += 1
		if R != None:
			nodeQueue.enqueue(R)
			numChildren += 1
		res += '1' if numChildren == 0 else '0'
	return res

# Helper functions
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
