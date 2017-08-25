# # Inequality
# concavity = buildTreeMapping('( sum_i log X_i / n )', 'log ( sum_i X_i / n )')

# # Equality
# expSumToProduct = buildTreeMapping('exp sum_i X_i', 'prod_i exp X_i')
# expProductToSum = buildTreeMapping('prod_i exp X_i', 'exp sum_i X_i')
# logProductToSum = buildTreeMapping('log prod_i X_i', 'sum_i log X_i')
# logSumToProduct = buildTreeMapping('sum_i log X_i', 'log prod_i X_i')
# independencePullOut = buildTreeMapping("E prod_i X_i", "prod_i E X_i")
# sumPushIn = buildTreeMapping('( t * sum_i X_i )', 'sum_i ( t * X_i )')
# sumPullOut = buildTreeMapping('sum_i ( t * X_i )', '( t * sum_i X_i )')

# # Density
conditional = buildTreeMapping('f ( x , y )', '( f ( x | y ) * f y )' )
# bayes = buildTreeMapping('f ( x | y )', '( f ( x , y ) / f y )')
# integrateOut = buildTreeMapping('f x', ' int ( f ( x , y ) , dy ) ')

# # Analysis
# # 0 <= p <= 1
# quadraticBound = buildTreeMapping('( p * ( 1 - p ) )', '1 / 4')
# # Taylor's expansion
# taylor = buildTreeMapping('f x', '( f y + ( d_dx f y * ( x - y ) ) )')
# expTaylor = buildTreeMapping('exp x', '( ( ( ( 1 + x ) + ( ( x ^ 2 ) / 2 ) ) + ( ( x ^ 3 ) / 6 ) )')
# # Differentiation
# differentiate = buildTreeMapping('( g * h )', '( ( g * d_dx h ) + ( h * d_dx g ) )')





# # from functools import partial
# # test = partial(applyFunList, funList = [symmetry, capBackwardAssociative, capForwardAssociative, invariant, symmetry])

# # # Helper function
# # def applyFunList(tree, funList):
# # 	for fun in funList:
# # 		tree = fun(tree)
# # 	return tree
