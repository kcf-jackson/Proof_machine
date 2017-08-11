def forwardAssociative(tree):
	# Code mapping: 22000 to 20200
	nodesList = mapTwoTuple(nodesList = treeToNodes(tree, '00111'), pos = [2,1], dictMap = getAssociativeDict())
	nodesDict = {1:2, 2:4, 3:1, 4:5, 5:3}
	return genericTreeMapping(nodesList, '20200', nodesDict)

def backwardAssociative(tree):
	# Code mapping: 20200 to 22000
	# nodesList refers to the original tree (including the nodeTreeIndicators)
	# position is the position of op1 and op2
	nodesList = mapTwoTuple(nodesList = treeToNodes(tree, '01011'), pos = [1,3], dictMap = getAssociativeDict())
	nodesDict = {1:3, 2:1, 3:5, 4:2, 5:4} 
	return genericTreeMapping(nodesList, '22000', nodesDict)

# Helper function
def getAssociativeDict():
	associativeDict = {
		('+', '+') : ('+', '+'),
		('+', '-') : ('+', '-'),
		('-', '+') : ('-', '-'),
		('-', '-') : ('-', '+'),
		('*', '*') : ('*', '*'),
		('*', '/') : ('*', '/'),
		('/', '*') : ('/', '/'),
		('/', '/') : ('/', '*'),
		('cup', 'cup') : ('cup', 'cup'),
		('cap', 'cap') : ('cap', 'cap')
	}
	return associativeDict

def mapTwoTuple(nodesList, pos, dictMap):
	originSym = (nodesList[pos[0] - 1].value, nodesList[pos[1] - 1].value)
	newSym = dictMap[originSym] 	
	nodesList[pos[0] - 1] = Node(newSym[0], 'operator')
	nodesList[pos[1] - 1] = Node(newSym[1], 'operator')
	return nodesList
