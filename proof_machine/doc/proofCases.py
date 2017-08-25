#==============================================================================
# Main
#==============================================================================
import os 
os.chdir('../')
exec(open('load.py').read())

# Proof of Markov's inequality
print("Markov's inequality")
lhs = parseTree("( a * I ( X >= a ) )")
op = "<="
rhs = parseTree("X")
masterEq = Equation(lhs, op, rhs)
masterEq.view()

masterEq.applyToBoth(div_X, Node('a', 'symbol'))
masterEq.applyToLeft(simplifyDiv)
masterEq.applyToBoth(takeExpectation)
masterEq.applyToLeft(functionalToMeasure)

# # Automatric proof of Markov's inequality
# print("We will derive the following result:")
# mainExpr = parseTree("( ( a * I ( X >= a ) ) - X )")
# targetExpr = parseTree("( a * P ( X >= a ) - E X )")
# print(treeToString(mainExpr) + " = " + treeToString(targetExpr))

# d1 = Derivation(mainExpr)
# funList = [inclusionExclusion, rightPushIn, symmetry, cupBackwardAssociative, capBackwardAssociative, \
# 			cupForwardAssociative, capForwardAssociative, invariant, symmetry, cupSimplify, capSimplify, 
# 			takeExpectation, functionalToMeasure, expectationPushIn, expectationPullOut, expectationSubPushIn, expectationSubPushIn]

# print("blindDerive: I supply a list of functions, the program applies a function whether it can. The order of application is random.")
# d1 = Derivation(mainExpr)
# d1.blindDerive(funList, 3, quiet = True)
# d1.view()
# print('End\n')

# print("semiAutoDerive: I supply a list of functions, the program returns a list of possible progression, and I tell the program how to progress.")
# d1 = Derivation(mainExpr)
# d1.semiAutoDerive(funList, quiet = True)
# d1.view()
# print('End\n')

# print("autoDerive: I supply a list of functions and a target expression, the program works its way out completely by itself.")
# d1 = Derivation(mainExpr)
# d1.autoDerive(targetExpr, funList, 8, quiet = True)
# print('End\n')
