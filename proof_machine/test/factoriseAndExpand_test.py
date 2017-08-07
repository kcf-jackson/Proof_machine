import os 
os.chdir('../')
exec(open('load.py').read())

print("Unit Testing for leftPushIn, leftPushOut, rightPushIn, rightPushOut")
expr = parseTree( "( c * ( a + b ) )")
print(' = '.join(map(treeToString, [expr, leftPushIn(expr), leftPullOut(leftPushIn(expr))])))

expr = parseTree( "( c / ( a - b ) )")
print(' = '.join(map(treeToString, [expr, leftPushIn(expr), leftPullOut(leftPushIn(expr))])))

expr = parseTree( "( ( a + b ) * c )")
print(' = '.join(map(treeToString, [expr, rightPushIn(expr), rightPullOut(rightPushIn(expr))])))

expr = parseTree( "( ( a - b ) / c )")
print(' = '.join(map(treeToString, [expr, rightPushIn(expr), rightPullOut(rightPushIn(expr))])))
