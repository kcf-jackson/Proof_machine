# def cauchySchwarz(tree):
# 	# Code mapping: 1200 to 1211220000
# 	nodesList = treeToNodes(tree, '0011') + [Node("sqrt", 'function'), Node('^', 'operator'), Node('2', 'symbol')]
# 	nodesDict = {1:5, 2:2, 3:1, 4:1, 5:6, 6:6, 7:3, 8:7, 9:4, 10:7}
# 	return genericTreeMapping(nodesList, '1211220000', nodesDict)

cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
inclusionExclusion = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
