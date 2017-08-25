# Expectation equality / inequality
# expectationPushIn = buildTreeMapping('E ( X + Y )', '( E X + E Y )') 
# expectationSubPushIn = buildTreeMapping('E ( X - Y )', '( E X - E Y )') 
# expectationPullOut = buildTreeMapping('( E X + E Y )', 'E ( X + Y )') 
# expectationSubPullOut = buildTreeMapping('( E X - E Y )', 'E ( X - Y )')

expectationLinearity = buildTreeMapping('E ( ( a * X ) + ( b * Y ) )', '( ( a * E X ) + ( b * E Y ) )') 

cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
jensen = buildTreeMapping('log E X', 'E log X')
