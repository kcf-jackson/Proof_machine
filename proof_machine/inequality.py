cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
inclusionExclusion = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
