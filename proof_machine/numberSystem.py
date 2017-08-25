realCommutative = buildTreeMapping('( m + n )', '( n + m )')

realAddLeftAssociative = buildTreeMapping('( k + ( m + n ) )', '( ( k + m ) + n )')
realAddRightAssociative = buildTreeMapping('( ( k + m ) + n )', '( k + ( m + n ) )')
realAddIdentity = buildTreeMapping('( m + 0 )', 'm')
realAddCancellation = buildTreeMapping('( k - k )', '0')

realMulLeftAssociative = buildTreeMapping('( k * ( m * n ) )', '( ( k * m ) * n )')
realMulRightAssociative = buildTreeMapping('( ( k * m ) * n )', '( k * ( m * n ) )')
realMulIdentity = buildTreeMapping('( m * 1 )', 'm')
realMulCancellation = buildTreeMapping('( k / k )', '1')

realLeftPushIn = buildTreeMapping('( k * ( m + n ) )', '( ( k * m ) + ( k * n ) )')
realLeftPullOut = buildTreeMapping('( ( k * m ) + ( k * n ) )', '( k * ( m + n ) )')
realRightPushIn = buildTreeMapping('( ( m + n ) * k )', '( ( m * k ) + ( n * k ) )')
realRightPullOut = buildTreeMapping('( ( m * k ) + ( n * k ) )', '( ( m + n ) * k )')
