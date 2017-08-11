import os 
os.chdir('../')
exec(open('load.py').read())


print("Basic test for LRcodeToBaseThreeCode and baseThreeCodeToLRCode")
print(baseThreeCodeToLRcode("2220000"))
print(LRcodeToBaseThreeCode("LL0LR0RL0RR0"))
print("End\n")


print("Unit test for LRcodeToBaseThreeCode and baseThreeCodeToLRCode")
testCases = ['0','1200', '110','10','200','2100','2010', '202010', '21100', '221000', '2220000', '212000', '211010', '120200']
for i in testCases:
	print(" ".join([i, baseThreeCodeToLRcode(i), LRcodeToBaseThreeCode(baseThreeCodeToLRcode(i))]))
print("End\n")


print("Unit test for LRcodeToBaseThreeCode and baseThreeCodeToLRCode")
print("Example 1")
printFullTree(LRcodeToTree('LR0'))
print("\n")

print("Example 2")
printFullTree(LRcodeToTree('LL0LR0R0'))
print("\n")

print("Example 3")
printFullTree(LRcodeToTree('L0RL0RR0'))
print("End\n")


print("Unit test for treeToNodes and relabelTree")
tree1 = LRcodeToTree("LL0LR0R0")
nodeList = treeToNodes(tree1)
for node in nodeList:
	print(node.value + ' ' + node.mathType)

tree2 = relabelTree(LRcodeToTree("LL0LR0R0"), nodeList[::-1])
nodeList = treeToNodes(tree2)
for node in nodeList:
	print(node.value + ' ' + node.mathType)
print("End\n")


print("Unit test for genericTreeMapping")
tree3 = LRcodeToTree("L0R0")
nodeList = treeToNodes(tree3)
for node in nodeList:
	print(node.value + ' ' + node.mathType)

tree4 = genericTreeMapping(tree3, treeMapCode = '200', nodesDict = {1:3, 2:4, 3:1}, addNodesList = [Node('new', 'symbol')])
nodeList = treeToNodes(tree4)
for node in nodeList:
	print(node.value + ' ' + node.mathType)
print("End\n")


print("Unit test for genericTreeMapping when children are trees")
tree3 = baseThreeCodeToTree("2200200")
printFullTree(tree3)

nodeList = treeToNodes(tree3, '0000100')
tree4 = genericTreeMapping(tree3, treeMapCode = '2022000', nodesDict = {1:1, 2:3, 3:2, 4:5, 5:4}, addNodesList = [], nodeTreeIndicator = '0000100')
printFullTree(tree4)
print("End\n")
