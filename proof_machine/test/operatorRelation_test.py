import os 
os.chdir('../')
exec(open('load.py').read())


print("Unit test for invariant")
expr = parseTree(" ( A cup A ) ")
expr.view()
invariant(expr).view()

expr = parseTree(" ( A cup B ) ")
expr.view()
invariant(expr).view()

expr = parseTree(" ( A cap A ) ")
expr.view()
invariant(expr).view()

expr = parseTree(" ( A cap B ) ")
expr.view()
invariant(expr).view()


print("Unit test for symmetric")
expr = parseTree(" ( a + b ) ")
expr.view()
symmetric(expr).view()

expr = parseTree(" ( a * b ) ")
expr.view()
symmetric(expr).view()


print("Unit test for tautology")
expr = parseTree(" ( a + b ) ")
expr.view()
tautology(expr, '+', '-', 'b').view()

expr = parseTree(" a ")
expr.view()
tautology(expr, '+', '-', 'b').view()

expr = parseTree(" X_n ")
expr.view()
tautology(expr, '+', '-', 'mu_n').view()
