from proof_machine import buildParseTree
from proof_machine.others import which
from proof_machine.objClass import Node, lookupPtype
from proof_machine.treeMap.treeEncoding import treeToBaseThreeCode, treeToLeavesCode
from proof_machine.treeMap.genericTreePattern import treeToNodes, genericTreeMapping

def buildTreeMapping(expr1, expr2, namespace):
	material = expressionToGenericMapping(expr1, expr2, namespace)	
	additionalNodes = list(map(lambda x: Node(x, lookupPtype(x, namespace)), material['extraSym']))
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

def expressionToGenericMapping(expr1, expr2, namespace, quiet = True):
	a1 = expressionAnalysis(expr1, namespace)
	a2 = expressionAnalysis(expr2, namespace)
	a1Sym = a1['symbolList']
	a2Sym = a2['symbolList']
	
	extraSym = symDiff(a1Sym, a2Sym)
	fullSym = a1Sym + extraSym
	mapDict = findMapping(fullSym, a2Sym)

	if not quiet:
		print("Leaves code: " + str(a1['leavesCode']))
		print("Symbol needed: " + ",".join(extraSym))
		print("Full symbol list: " + ",".join(fullSym))
		print("Dictionary:")
		print(mapDict)
		print("Tree code: " + str(a2['treeCode']))
	return {'srcNodesList': a1['nodesList'], 'leavesCode': a1['leavesCode'], 'extraSym': extraSym, \
			'fullSym': fullSym, 'treeMapCode': a2['treeCode'], 'mapDict': mapDict}

# Analyse an expression and decompose into 'tree, codes, nodesList, symList'
def expressionAnalysis(expr1, namespace):
	tree = buildParseTree(expr1, namespace)
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
