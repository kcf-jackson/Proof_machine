#==============================================================================
# General setup
#==============================================================================
exec(open('factory//patternConversion.py').read())
exec(open('factory//treeCreation.py').read())
exec(open('manipulation//arithmetic.py').read())
exec(open('manipulation//associativeLaw.py').read())
exec(open('manipulation//factoriseAndExpand.py').read())
exec(open('manipulation//operatorRelation.py').read())
exec(open('manipulation//simplify.py').read())
exec(open('objClass//classDerivation.py').read())
exec(open('objClass//classEquation.py').read())
exec(open('objClass//classTree.py').read())
exec(open('util.py').read())

parenthesesList = ['{', '[', '(', ')', ']', '}']
unaryFunctionList = ['E', 'I', 'P', 'exp', 'log', 'cup_i', 'sum_i']
unaryOpList = parenthesesList + unaryFunctionList
binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>', 'cup', 'cap']
opList = unaryOpList + binaryOpList
variableState = {'a': ['constant'], 'b': ['constant'], 'X': ['random variable'], 'I': ['function']}

# Functions that require initialisation
parseTree = partial(buildParseTree, unaryOpList = unaryOpList, binaryOpList = binaryOpList)
