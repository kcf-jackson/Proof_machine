# Associative law
def forwardAssociative(tree):
	#(a op1 b) op2 c = a op1 (b op2 c)
	associativeDict = {'++': '++', '+-': '+-', '-+': '--', '--': '-+', \
						'**': '**', '*/': '*/', '/*' : '//', '//': '/*'}
	op1 = tree.getLeftChildValue()
	op2 = tree.getRootNodeValue()
	if op1 + op2 in associativeDict:
		newop1, newop2 = associativeDict[op1 + op2]
		return twoOneHorizontalToOneTwoHorizontal(tree, Node(newop1, 'operator'), Node(newop2, 'operator'))
	elif op1 == op2 == 'cup' or op1 == op2 == 'cap':
		newop1 = newop2 = op1
		return twoOneHorizontalToOneTwoHorizontal(tree, Node(newop1, 'operator'), Node(newop2, 'operator'))
	return tree

def backwardAssociative(tree):
	#Code mapping: 20200 to 22000
	#a op1 (b op2 c) = (a op1 b) op2 c
	associativeDict = {'++': '++', '+-': '+-', '-+': '--', '--': '-+', \
						'**': '**', '*/': '*/', '/*' : '//', '//': '/*'}
	op1 = tree.getRootNodeValue()
	op2 = tree.getRightChildValue()
	if op1 + op2 in associativeDict:
		newop1, newop2 = associativeDict[op1 + op2]
		return oneTwoHorizontalToTwoOneHorizontal(tree, Node(newop2, 'operator'), Node(newop1, 'operator'))
	elif op1 == op2 == 'cup' or op1 == op2 == 'cap':
		newop1 = newop2 = op1
		return oneTwoHorizontalToTwoOneHorizontal(tree, Node(newop2, 'operator'), Node(newop1, 'operator'))
	return tree

def compoundAssociative(tree):
	#Code mapping: 2220000 to 2202000
	if tree.getRootNodeValue() in ['+', '*', 'cap', 'cup']:
		if tree.getRootNodeValue() == tree.getLeftChildValue() and tree.getLeftChildValue() == tree.getRightChildValue():
			nodesDict = {1:3, 2:1, 3:7, 4:2, 5:6, 6:4, 7:5}
			return genericTreeMapping(tree, '2202000', nodesDict, newNodesList = [])
	return tree
