# Probability equality / inequality

# Equality
pInclusionExclusion = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')

# Inequality; LHS leq RHS; X > 0, a > 0 
markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
chernoff = buildTreeMapping('P ( norm sum_i X_i >= ( k * sigma ) )', 'exp ( ( 0 - ( k ^ 2 ) ) / ( 4 * n ) )')

# Inequality; LHS leq RHS; any R.V. X, Y, 
unionBound = buildTreeMapping('P ( ( X + Y ) >= x )', '( P ( X >= ( x / 2 ) ) + P ( Y >= ( x / 2 ) ) )')
unionAbsBound = buildTreeMapping('P ( abs ( X + Y ) >= x )', '( P ( abs X >= ( x / 2 ) ) + P ( abs Y >= ( x / 2 ) ) )')

# Inequality; LHS leq RHS; IID X, Y, a > 0
sumDiffBound = buildTreeMapping('P ( abs ( X + Y ) <= a )', '( 2 * P ( abs ( X - Y ) <= a ) )')

# Inequality; LHS geq RHS; X, Y independent
invUnionBound = buildTreeMapping('P ( ( X + Y ) <= x )', '( P ( X <= ( x / 2 ) ) * P ( Y <= ( x / 2 ) ) )')
unvUnionAbsBound = buildTreeMapping('P ( abs ( X + Y ) <= x )', '( P ( abs X <= ( x / 2 ) ) * P ( abs Y <= ( x / 2 ) ) )')
