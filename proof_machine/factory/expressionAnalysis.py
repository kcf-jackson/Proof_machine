def buildTreeMapping(expr1, expr2):
	material = expressionToGenericMapping(expr1, expr2)	
	additionalNodes = list(map(lambda x: Node(x, whatType(x, typeDict)), material['extraSym']))
	benchmarkSignature = subsetNodesList(material['srcNodesList'], material['leavesCode'])
	def treeFunction(tree):
		treeSignature = getTreeSignature(tree, material['leavesCode'])
		signatureCheck = passTreeSignature(treeSignature, benchmarkSignature)
		if signatureCheck:
			# try:
			nodesList = treeToNodes(tree, material['leavesCode']) + additionalNodes
			nodesDict = material['mapDict']
			res = genericTreeMapping(nodesList, material['treeMapCode'], nodesDict)
			return res
			# except:
				# return tree
		else:
			return tree
	return treeFunction

def expressionToGenericMapping(expr1, expr2, quiet = True):
	a1 = expressionAnalysis(expr1)
	a2 = expressionAnalysis(expr2)
	a1Sym = a1['symbolList']
	a2Sym = a2['symbolList']
	
	extraSym = symDiff(a1Sym, a2Sym)
	fullSym = a1Sym + extraSym
	treeMapCode = a2['treeCode']
	leavesCode = a1['leavesCode']
	mapDict = findMapping(fullSym, a2Sym)

	if not quiet:
		print("Leaves code: " + str(leavesCode))
		print("Symbol needed: " + ",".join(extraSym))
		print("Full symbol list: " + ",".join(fullSym))
		print("Dictionary:")
		print(mapDict)
		print("Tree code: " + str(treeMapCode))
	return {'srcNodesList': a1['nodesList'], 'leavesCode': leavesCode, 'extraSym': extraSym, \
			'fullSym': fullSym, 'treeMapCode': treeMapCode, 'mapDict': mapDict}

# Analyse an expression and decompose into 'tree, codes, nodesList, symList'
def expressionAnalysis(expr1):
	tree = parseTree(expr1)
	treeCode = treeToBaseThreeCode(tree)
	leavesCode = treeToLeavesCode(tree)
	nodesList = treeToNodes(tree)
	symList = list(map(lambda x: x.value, nodesList))
	return {'tree': tree, 'treeCode': treeCode, 'leavesCode': leavesCode, 'nodesList': nodesList, 'symbolList': symList}

# Find the extra symbol in symbol list 2
def symDiff(symList1, symList2):
	return sorted(list(set(symList2) - set(symList1)))

# Given symbol list 1 and 2, find the possible mapping
def findMapping(symList1, symList2):
	mapDict = {}
	for ind, i in enumerate(symList2):
		pos = list(map(lambda x: x+1, which(symList1, i)))
		# if len(pos) == 1:
		pos = pos[0]	
		mapDict[ind + 1] = pos
	return mapDict

# Helper functions
def which(l0, element):
	res = []
	for ind, i in enumerate(l0):
		if i == element:
			res.append(ind)
	return res

def getTreeSignature(tree, leavesCode):
	nodesList = treeToNodes(tree, leavesCode)
	return subsetNodesList(nodesList, leavesCode)

def subsetNodesList(l0, indicator):
	return [node for ind, node in enumerate(l0) if indicator[ind] == '0']	

def passTreeSignature(nodesList1, nodesList2):
	for ind, nodeFromList1 in enumerate(nodesList1):
		nodeFromList2 = nodesList2[ind]
		if nodeFromList1 != nodeFromList2:
			return False
	return True
