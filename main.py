#==============================================================================
# General setup
#==============================================================================
exec(open('classEquation.py').read())
exec(open('classTree.py').read())
exec(open('treeMethods.py').read())
exec(open('util.py').read())

parenthesesList = ['{', '[', '(', ')', ']', '}']
unaryFunctionList = ['E', 'I', 'P', 'exp', 'log']
unaryOpList = parenthesesList + unaryFunctionList
binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>']
opList = unaryOpList + binaryOpList
variableState = {'a': ['constant'], 'b': ['constant'], 'X': ['random variable'], 'I': ['function']}


parseTree = partial(buildParseTree, unaryOpList = unaryOpList, binaryOpList = binaryOpList)

#==============================================================================
# Main
#==============================================================================
# Proof of Markov's inequality
lhs = parseTree("( a * I ( X >= a ) )")
op = "<="
rhs = parseTree("X")
masterEq = Equation(lhs, op, rhs)
masterEq.view()

masterEq.applyToBoth(div_X, Node('a', 'symbol'))
masterEq.applyToLeft(simplifyDiv)
masterEq.applyToBoth(takeExpectation)
masterEq.applyToLeft(functionalToMeasure)
