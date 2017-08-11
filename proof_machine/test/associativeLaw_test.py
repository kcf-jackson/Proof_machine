import os 
os.chdir('../')
exec(open('load.py').read())

print("Unit test for forwardAssoicative and backwardAssociative")
expr = parseTree( "( ( a + b ) - c )" )
expr.view()
forwardAssociative(expr).view()
backwardAssociative(forwardAssociative(expr)).view()

print("\n")
expr = parseTree( "( ( a - b ) - c )" )
expr.view()
forwardAssociative(expr).view()
backwardAssociative(forwardAssociative(expr)).view()

expr = parseTree( "( ( a + b ) + ( c + d ) )" )
expr.view()
backwardAssociative(expr).view()
forwardAssociative(backwardAssociative(expr)).view()
forwardAssociative(expr).view()
