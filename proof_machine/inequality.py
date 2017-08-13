# Inequality
cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
chernoff = buildTreeMapping('P ( abs sum_i X_i >= ( k * sigma ) )', 'exp ( ( 0 - ( k ^ 2 ) ) / ( 4 * n ) )')
jensen = buildTreeMapping('log E X', 'E log X')
concavity = buildTreeMapping('( sum_i log X_i / n )', 'log ( sum_i X_i / n )')

# Equality
expSumToProduct = buildTreeMapping('exp sum_i X_i', 'prod_i exp X_i')
expProductToSum = buildTreeMapping('prod_i exp X_i', 'exp sum_i X_i')
logProductToSum = buildTreeMapping('log prod_i X_i', 'sum_i log X_i')
logSumToProduct = buildTreeMapping('sum_i log X_i', 'log prod_i X_i')

inclusionExclusionP = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
inclusionExclusion = buildTreeMapping('I ( A cup B )', '( ( I A + I B ) - I ( A cap B ) )')
independencePull = buildTreeMapping("E prod_i X_i", "prod_i E X_i")

sumPushIn = buildTreeMapping('( t * sum_i X_i )', 'sum_i ( t * X_i )')
sumPullOut = buildTreeMapping('sum_i ( t * X_i )', '( t * sum_i X_i )')

forwardAssociativeCup = buildTreeMapping('( ( A cup B ) cup C )', '( A cup ( B cup C ) )')
backwardAssociativeCup = buildTreeMapping('( ( A cup B ) cup C )', '( A cup ( B cup C ) )')

forwardAssociativeCap = buildTreeMapping('( ( A cap B ) cap C )', '( A cap ( B cap C ) )')
backwardAssociativeCap = buildTreeMapping('( ( A cap B ) cap C )', '( A cap ( B cap C ) )')
