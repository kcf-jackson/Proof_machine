# Set operation
inclusionExclusion = buildTreeMapping('I ( A cup B )', '( ( I A + I B ) - I ( A cap B ) )')

cupForwardAssociative = buildTreeMapping('( ( A cup B ) cup C )', '( A cup ( B cup C ) )')
cupBackwardAssociative = buildTreeMapping('( ( A cup B ) cup C )', '( A cup ( B cup C ) )')
capForwardAssociative = buildTreeMapping('( ( A cap B ) cap C )', '( A cap ( B cap C ) )')
capBackwardAssociative = buildTreeMapping('( ( A cap B ) cap C )', '( A cap ( B cap C ) )')

cupSimplify = buildTreeMapping('( ( A cup B ) cup ( C cup B ) )', '( ( A cup B ) cup C ) ')
capSimplify = buildTreeMapping('( ( A cap B ) cap ( C cap B ) )', '( ( A cap B ) cap C ) ')
cupDeMorgan = buildTreeMapping('cplm ( A cup B )', '( cplm A cap cplm B )')
capDeMorgan = buildTreeMapping('cplm ( A cap B )', '( cplm A cup cplm B )')

setUpperBound = buildTreeMapping('I cup_i A_i', 'sum_i I A_i')

# Useful decompositions
decomposition_1 = buildTreeMapping('X', '( ( X * I ( X <= E X ) ) + ( X * I ( X > E X ) ) )')

# def subsetTechnique(tree, method):
# 	if method = 'monotone':
# 		addOneNodeOnTop(tree, Node('g', 'function', 'monotone'))
# 	elif method = 'absolute'
# 	