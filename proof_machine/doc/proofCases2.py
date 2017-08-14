import os 
os.chdir('../')
exec(open('load.py').read())


print("We will derive the following result:")
mainExpr = parseTree(" I ( ( A cup B ) cup C ) ")
targetExpr = parseTree("( ( ( ( ( ( I A + I B ) + I C ) - I ( A cap B ) ) - I ( A cap C ) ) - I ( B cap C ) ) + I ( ( A cap B ) cap C ) )")
print(treeToString(mainExpr) + " = " + treeToString(targetExpr))


print("Here is the manual approach. I guide the program to derive step-by-step.")

d1 = Derivation(mainExpr)
d1.derive(inclusionExclusion)

expr1 = parseTree(" I ( A cup B ) ")
d1.substitute(expr1, inclusionExclusion)

expr2 = parseTree(" ( ( A cup B ) cap C ) ")
d1.substitute(expr2, rightPushIn)

expr3 = parseTree(" I ( ( A cap C ) cup ( B cap C ) ) ")
d1.substitute(expr3, inclusionExclusion)

expr4 = parseTree(" ( B cap C ) ")
d1.substitute(expr4, symmetry)

expr5 = parseTree(" ( ( A cap C ) cap ( C cap B ) ) ")
d1.substitute(expr5, backwardAssociative)

expr6 = parseTree(" ( ( A cap C ) cap C ) ")
d1.substitute(expr6, forwardAssociative)

expr7 = parseTree(" ( C cap C ) ")
d1.substitute(expr7, invariant)

d1.derive(backwardAssociative)

d1.view()
print('End\n')


print("Here is the automatic approach.")
d1 = Derivation(mainExpr)
funList = [inclusionExclusion, rightPushIn, symmetry, cupBackwardAssociative, capBackwardAssociative, \
			cupForwardAssociative, capForwardAssociative, invariant, symmetry, cupSimplify, capSimplify]

print("blindDerive: I supply a list of functions, the program applies a function whether it can. The order of application is random.")
d1 = Derivation(mainExpr)
d1.blindDerive(funList, 3, quiet = True)
d1.view()
print('End\n')

print("semiAutoDerive: I supply a list of functions, the program returns a list of possible progression, and I tell the program how to progress.")
d1 = Derivation(mainExpr)
d1.semiAutoDerive(funList, quiet = True)
d1.view()
print('End\n')

print("autoDerive: I supply a list of functions and a target expression, the program works its way out completely by itself.")
d1 = Derivation(mainExpr)
d1.autoDerive(targetExpr, funList, 8, quiet = True)
print('End\n')
