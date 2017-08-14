import os 
os.chdir('../')
exec(open('load.py').read())
exec(open('theorems.py').read())


# Unit test
print("Unit test for inclusion-exclusion principle")
expr = parseTree(" I ( A cup B ) ")
# Equation(expr, "=", inclusion_exclusion(expr)).view()
Equation(expr, "=", inclusionExclusion(expr)).view()

expr = parseTree(" I ( ( A cup B ) cup C )")
eq = Equation(expr, "=", inclusionExclusion(expr))
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

mainExpr = parseTree(" I ( ( A cup B ) cup C ) ")
d1 = Derivation(mainExpr)
d1.derive(inclusionExclusion)
d1.substitute(expr1, inclusionExclusion)
d1.substitute(expr2, rightPushIn)
d1.substitute(expr3, inclusionExclusion)
d1.substitute(expr4, symmetry)
d1.substitute(expr5, backwardAssociative)
d1.substitute(expr6, forwardAssociative)
d1.substitute(expr7, invariant)
d1.derive(backwardAssociative)
# d1.derive(symmetry)
d1.view()
print('End\n')


# Unit test
print("Unit test for autoDerive")
d1 = Derivation(mainExpr)
funList = [inclusionExclusion, rightPushIn, symmetry, cupBackwardAssociative, capBackwardAssociative, \
			cupForwardAssociative, capForwardAssociative, invariant, symmetry, cupSimplify, capSimplify]

print("Depth, randomised and unsupervised")
d1 = Derivation(mainExpr)
d1.blindDerive(funList, 3, quiet = True)
d1.view()

# print("Breadth, supervised")
# d1 = Derivation(mainExpr)
# d1.semiAutoDerive(funList, quiet = True)
# d1.view()

print("Breadth, unsupervised")
d1 = Derivation(mainExpr)
targetExpr = parseTree("( ( ( ( ( ( I A + I B ) + I C ) - I ( A cap B ) ) - I ( A cap C ) ) - I ( B cap C ) ) + I ( ( A cap B ) cap C ) )")
d1.autoDerive(targetExpr, funList, 10, quiet = True)
print('End\n')


# # Unit test
# print("Unit test for analytic expression")
# expr = parseTree('f x')
# taylor(expr).view()

# expr = parseTree('( g * h )')
# differentiate(expr).view()
