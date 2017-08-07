import os 
os.chdir('../')
exec(open('load.py').read())
exec(open('theorems.py').read())


# Unit test
print("Unit test for inclusion-exclusion principle")
expr = parseTree(" I ( A cup B ) ")
eq = Equation(expr, "=", inclusion_exclusion(expr))
eq.view()

expr = parseTree(" I ( ( A cup B ) cup C )")
eq = Equation(expr, "=", inclusion_exclusion(expr))
eq.view()
print('End\n')


# Unit test
print("Unit test for substitute and derive")
expr1 = parseTree(" I ( A cup B ) ")
expr2 = parseTree(" ( ( A cup B ) cap C ) ")
expr3 = parseTree(" I ( ( A cap C ) cup ( B cap C ) ) ")
expr4 = parseTree(" ( B cap C ) ")
expr5 = parseTree(" ( ( A cap C ) cap ( C cap B ) ) ")
expr6 = parseTree(" ( ( A cap C ) cap C ) ")
expr7 = parseTree(" ( C cap C ) ")

forwardAssociative(expr6).view()

mainExpr = parseTree(" I ( ( A cup B ) cup C ) ")
d1 = Derivation(mainExpr)
d1.derive(inclusion_exclusion)
d1.substitute(expr1, inclusion_exclusion)
d1.substitute(expr2, rightPushIn)
d1.substitute(expr3, inclusion_exclusion)
d1.substitute(expr4, symmetric)
d1.substitute(expr5, compoundAssociative)
d1.substitute(expr6, forwardAssociative)
d1.substitute(expr7, invariant)
d1.view()
print('End\n')

# # Unit test
# print("Unit test for upper bound of indicators.")
# expr = parseTree("I cup_i A_i")
# eq = Equation(expr, "<=", indicatorSumUpperBound(expr))
# eq.view()
