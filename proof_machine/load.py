#==============================================================================
# General setup
#==============================================================================
exec(open('factory//basicTreePattern.py').read())
exec(open('factory//genericTreePattern.py').read())
exec(open('factory//treeEncoding.py').read())
exec(open('factory//treeEquality.py').read())
exec(open('manipulation//arithmetic.py').read())
exec(open('manipulation//associativeLaw.py').read())
exec(open('manipulation//factoriseAndExpand.py').read())
exec(open('manipulation//operatorRelation.py').read())
exec(open('manipulation//simplify.py').read())
exec(open('objClass//classDerivation.py').read())
exec(open('objClass//classEquation.py').read())
exec(open('objClass//classTree.py').read())
exec(open('factory//expressionAnalysis.py').read())
exec(open('functionDict.py').read())
exec(open('util.py').read())

parenthesesList = ['{', '[', '(', ')', ']', '}']
unaryFunctionList = ['E', 'I', 'P', 'exp', 'log', 'cup_i', 'sum_i', 'prod_i', 'sqrt', 'abs']
binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>', 'cup', 'cap']
import string
variableList = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase)

opList = parenthesesList + unaryFunctionList + binaryOpList + variableList
# variableState = {'a': ['constant'], 'b': ['constant'], 'X': ['random variable'], 'I': ['function']}

# Functions that require initialisation
parseTree = partial(buildParseTree, unaryOpList = parenthesesList + unaryFunctionList, binaryOpList = binaryOpList)
typeDict = buildTypeDict(opList, parenthesesList, unaryFunctionList, binaryOpList, variableList)

# File that uses parseTree
exec(open('inequality.py').read())
