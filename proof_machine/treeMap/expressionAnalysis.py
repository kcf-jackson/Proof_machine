from proof_machine import buildParseTree
from proof_machine.others import which
from proof_machine.objClass import Node, lookupPtype
from proof_machine.treeMap.treeEncoding import treeToBaseThreeCode, treeToLeavesCode
from proof_machine.treeMap.genericTreePattern import treeToNodes, genericTreeMapping

def buildTreeMapping(expr1, expr2, namespace):
	tree1 = buildParseTree(expr1, namespace)
	tree2 = buildParseTree(expr2, namespace)
	mapSpec = getNodesMapping(tree1, tree2)	
	extraNodes = convertSymbolToNodes(mapSpec['extraSym'], namespace)
	sourceSignature = getTreeSignature(tree1)
	sourceTreeCode = treeToLeavesCode(tree1)
	targetMapCode = treeToBaseThreeCode(tree2)
	def treeFunction(tree, quiet = True):
		treeSignature = getTreeSignature(tree)
		signatureCheck = passTreeSignature(treeSignature, sourceSignature, quiet)
		if signatureCheck:
			nodesList = treeToNodes(tree, sourceTreeCode) + extraNodes
			res = genericTreeMapping(nodesList, targetMapCode, mapSpec['mapDict'])
			return res
		else:
			return tree
	return treeFunction


# Mapping between two trees
def convertSymbolToNodes(symbolList, namespace):
	return [Node(x, lookupPtype(x, namespace)) for x in symbolList]

def getNodesMapping(tree1, tree2):
	a1Sym = getSymbolList(tree1)
	a2Sym = getSymbolList(tree2)
	
	extraSym = symDiff(a1Sym, a2Sym)
	mapDict = findMapping(a1Sym + extraSym, a2Sym)

	return {'extraSym': extraSym, 'mapDict': mapDict}

def getSymbolList(tree):
	nodesList = treeToNodes(tree)
	symList = [x.value for x in nodesList]
	return symList

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


# Signature functions
def getTreeSignature(tree):
	# signature is a pair of nodes list: parents, children
	baseThreeCodes = treeToBaseThreeCode(tree)
	nodesList = treeToNodes(tree)
	parentsIndicator = [x != '0' for x in baseThreeCodes]
	childrenIndicator = [x == '0' for x in baseThreeCodes]
	return {'parentsSignature': subsetList(nodesList, parentsIndicator), \
			'childrenSignature': subsetList(nodesList, childrenIndicator)}

def showTreeSignature(sign1):
	print("Parents signature:")
	print([x.View() for x in sign1['parentsSignature']])
	print("Children signature:")
	print([x.View() for x in sign1['childrenSignature']])

def subsetList(l0, indicator):
	return [node for ind, node in enumerate(l0) if indicator[ind]]	

def passTreeSignature(sign1, sign2, quiet = True):
	# signature 2 is the benchmark / source signature
	if not quiet:
		showTreeSignature(sign1)
		showTreeSignature(sign2)
	# signature is a pair of nodes list: parents, children
	return compareParentsSignature(sign1['parentsSignature'], sign2['parentsSignature']) and \
			compareChildrenSignature(sign1['childrenSignature'], sign2['childrenSignature'])

def compareParentsSignature(sign1, benchmarkSign):
	# signature is a pair of nodes list: parents, children
	for ind, n1 in enumerate(sign1):
		n2 = benchmarkSign[ind]
		if n1 != n2:
			return False
	return True

def compareChildrenSignature(sign1, benchmarkSign):
	# signature is a pair of nodes list: parents, children
	for ind, s1 in enumerate(sign1):
		s2 = benchmarkSign[ind]
		if not compareChildrenNodes(s1, s2):
			return False
	return True

def compareChildrenNodes(node1, benchmarkNode):
	return all([x in node1.state for x in benchmarkNode.state])
