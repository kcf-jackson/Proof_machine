import os 
os.chdir('../')
exec(open('load.py').read())

print("Unit test for expressionToGenericMapping")
print("Cauchy Schwarz's inequality")
expressionToGenericMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 

cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
cauchySchwarz(parseTree('E ( X * Y )')).view()
print("End\n")
# see inequality.py
# def cauchySchwarz(tree):
# 	# Code mapping: 1200 to 1211220000
# 	nodesList = treeToNodes(tree, '0011') + [Node("sqrt", 'function'), Node('^', 'operator'), Node('2', 'symbol')]
# 	nodesDict = {1:5, 2:2, 3:1, 4:1, 5:6, 6:6, 7:3, 8:7, 9:4, 10:7}
# 	return genericTreeMapping(nodesList, '1211220000', nodesDict)

print("\nMarkov's inequality")
expressionToGenericMapping('P ( X >= a )', '( E X / a )') 
def markov(tree):
	nodesList = treeToNodes(tree, '0011') + [Node('/', 'operator'), Node("E", 'function')]
	nodesDict = {1: 5, 2: 6, 3: 4, 4: 3}
	return genericTreeMapping(nodesList, '2100', nodesDict)
expr1 = parseTree('P ( X >= a )')
markov(expr1).view()

markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
markov(expr1).view()
print("End\n")


print("\nInclusion/Exclusion principle")
expressionToGenericMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
def inclusionExclusion(tree):
	nodesList = treeToNodes(tree, '0011') + [Node('+', 'operator'), Node('-', 'operator'), Node("cap", 'operator')]
	nodesDict = {1: 6, 2: 5, 3: 1, 4: 1, 5: 1, 6: 7, 7: 3, 8: 4, 9: 3, 10: 4}
	return genericTreeMapping(nodesList, '2211120000', nodesDict)
expr1 = parseTree('P ( A cup B )')
inclusionExclusion(expr1).view()
print("End\n")


print("Unit test for buildTreeMapping")
inclusionExclusion = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
expr1 = parseTree('P ( A cup B )')
inclusionExclusion(expr1).view()

expr2 = parseTree('P ( A cup ( B cup C ) )')
inclusionExclusion(expr2).view()
print("End\n")