# Tree equality
# def treeEqualityByNodeValues(tree1, tree2):


# def treeEqualityByNodeTypes(tree1, tree2):

def treeEqualityByStructure(tree1, tree2):
	return treeToBaseThreeCodes(tree1) == treeToBaseThreeCodes(tree2)

# Compute a difference score between two trees
def treeDiff(tree1, tree2):
	countDict1 = countNodes(tree1)
	countDict2 = countNodes(tree2)
	diff = 0
	for item in countDict1:
		if item in countDict2:
			diff += abs(countDict1[item] - countDict2[item])
		else:
			diff += countDict1[item]
	for item in countDict2:
		if item not in countDict1:
			diff += countDict2[item]
	return diff

# Count each symbol in a tree
def countNodes(tree1):
	nodesList = treeToNodes(tree1)
	symList = [x.value for x in nodesList]
	key = set(symList)
	countDict = {}
	for k in key:
		countDict[k] = symList.count(k)
	return countDict

# Compute a list of difference scores from a tree
def treeDiffList(tree, treeList):
	return [treeDiff(tree, x) for x in treeList]

# Find the tree with the minimum difference in a list
def minDiffTree(tree, treeList):
	import random
	scoreList = treeDiffList(tree, treeList)
	index = (which(scoreList, min(scoreList)))
	index = ifelse(len(index) > 1, random.sample(index, 1)[0], index[0])
	return treeList[index]
