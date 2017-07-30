from pythonds.basic.stack import Stack
exec(open('classNode.py').read())


def buildParseTree(fpexp, unaryOpList, binaryOpList):
	tokenList = fpexp.split()   # Expression to be parsed
	exprTree = BinaryTree('')   # Expression Tree
	parentStack = Stack()       # Keep track of the parent node
	parentStack.push(exprTree)  

	currentTree = exprTree
	for i in tokenList:
		if i in unaryOpList:
			if i in parenthesesList[0:3]:
			# if it is an open parentheses
				currentTree.setRootNode(Node(i, 'parentheses'))	
				currentTree.insertLeft('')
				parentStack.push(currentTree)
				currentTree = currentTree.getLeftChild()
			elif i in unaryFunctionList:
			# if it is an unary function
				currentTree.setRootNode(Node(i, 'function'))
				currentTree.insertLeft('')
				parentStack.push(currentTree)
				currentTree = currentTree.getLeftChild()		
			elif i in parenthesesList[3:6]:
			# if it is a close parentheses
				currentTree = parentStack.pop()
				if currentTree.getRootNodeType() == 'function':
					currentTree = parentStack.pop()
		elif i in binaryOpList:
			# if it is an binary operator
			currentTree.setRootNode(Node(i, 'operator'))
			currentTree.insertRight('')
			parentStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i not in binaryOpList and i not in parenthesesList[3:6]:
			# if it is a constant or symbol (leaf)
			currentTree.setRootNode(Node(i, 'symbol'))
			currentTree = parentStack.pop()  # move up one level
		else:
			raise ValueError
	return exprTree


# # Unit test
# if __name__ == '__main__':
# 	exec(open('exprTreeMethods.py').read())
# 	parenthesesList = ['{', '[', '(', ')', ']', '}']
# 	unaryFunctionList = ['E', 'I']
# 	unaryOpList = parenthesesList + unaryFunctionList
# 	binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>']
# 	OpList = unaryOpList + binaryOpList

# 	pt = buildParseTree("( ( ( 10 + 5 ) * 3 ) <= 50 )", unaryOpList, binaryOpList)
# 	print(treeToString(pt))

# 	pt = buildParseTree("( X >= a )", unaryOpList, binaryOpList)
# 	print(treeToString(pt))

# 	pt = buildParseTree("I ( X >= a )", unaryOpList, binaryOpList)
# 	print(treeToString(pt))

# 	pt = buildParseTree("( a * I { X >= a } )", unaryOpList, binaryOpList)
# 	print(treeToString(pt))

# 	pt = buildParseTree("( ( a * I ( X >= a ) ) <= X )", unaryOpList, binaryOpList)
# 	print(treeToString(pt))

# 	pt = takeExpectation(pt)
# 	print(treeToString(pt))

# 	# printFullTree(pt)
