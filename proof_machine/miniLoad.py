# exec(open('factory//basicTreePattern.py').read())
# exec(open('factory//genericTreePattern.py').read())
# exec(open('factory//expressionAnalysis.py').read())
# exec(open('factory//treeEncoding.py').read())
# exec(open('factory//treeEquality.py').read())
# exec(open('objClass//classTree.py').read())
# exec(open('objClass//classDerivation.py').read())
exec(open('util.py').read())

def defaultNamespace():
	# Symbols
	alphaNumeric = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase)
	greekAlphabet = ['alpha', 'beta', 'chi', 'delta', 'digamma', 'epsilon', 'eta', 'gamma', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'omega', 
		'phi', 'pi', 'psi', 'rho', 'sigma', 'tau', 'theta', 'upsilon', 'varepsilon', 'varkappa', 'varphi', 'varpi', 'varrho', 'varsigma', 
		'vartheta', 'xi', 'zeta', 'Delta', 'Gamma', 'Lambda', 'Omega', 'Phi', 'Pi', 'Psi', 'Sigma', 'Theta', 'Upsilon', 'Xi', 'mho', 'nabla']
	# Functions
	trigonometricFunction = ['sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'arcsec', 'arccsc', 'arccot']
	hyperbolicFunction = ['sinh', 'cosh', 'tanh', 'sech', 'csch', 'coth', 'arsinh', 'arcosh', 'artanh', 'arsech', 'arcsch', 'arcoth']
	elementaryFunction = ['exp', 'log', 'abs', 'sqrt', 'max', 'min']
	setFunction = ['I', 'sup', 'inf', 'limsup', 'liminf', 'cap_i', 'cup_i', 'cplm']
	integrationFunction = ['int', 'D']
	probabilityFunction = ['E', 'P']
	arithmeticFunction = ['sum_i', 'prod_i']
	vectorSpaceFunction = ['norm']
	# Operators
	arithmeticOperator = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=']
	logicOperator = ['=>', '<=>', 'land', 'lor']
	setOperator = ['cup', 'cap', 'setDiff', 'symSetDiff']
	otherOperator = ['|', ',']

def addIndexToVariable(variable, numIndex):
	[variable + "_" + str(x) for x in list(range(numIndex + 1))]




globalVariables.modifyVariableState('f', ['function', 'random'])
globalVariables.defineVariable("x_1", 'scalar')
globalVariables.View()

# parenthesesList = ['{', '[', '(', ')', ']', '}']
# unaryFunctionList = ['E', 'I', 'P', 'exp', 'log', 'cup_i', 'sum_i', 'prod_i', 'sqrt', 'abs', 'cplm', \
# 					'D', 'f', 'g', 'norm', 'sup', 'inf', 'limsup', 'liminf', 'int']
# binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>', 'cup', 'cap', 'setDiff', 'symSetDiff', '|', ',']


# import string
# variableList = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase)


# opList = parenthesesList + unaryFunctionList + binaryOpList + variableList
# variableState = {'a': ['constant'], 'b': ['constant'], 'X': ['random variable'], 'Y': ['random variable'], 'I': ['function']}

# # Functions that require initialisation
# from functools import partial
# parseTree = partial(buildParseTree, unaryOpList = parenthesesList + unaryFunctionList, binaryOpList = binaryOpList, symbolStateDict = variableState)
# typeDict = buildTypeDict(opList, parenthesesList, unaryFunctionList, binaryOpList, variableList)


# integrateOut = buildTreeMapping('( f x * int D y )', 'int ( f ( x , y ) * D y )' )
# conditional = buildTreeMapping('f ( x , y )', '( f ( x | y ) * f y )' )
# conditional2 = buildTreeMapping('f ( x , y )', '( f ( y | x ) * f x )' )
# bayes = buildTreeMapping('f ( x | y )', '( f ( x , y ) / f y )')
# symmetry = buildTreeMapping('( x , y )', '( y , x )')
# associative = buildTreeMapping('( ( x , y ) , z )', '( x , ( y , z ) )')

# # expr = parseTree('f ( y , z )')
# # conditional(expr).view()

# expr = parseTree('f ( theta | ( x , y ) )')
# # integrateOut(expr).view()

# d1 = Derivation(expr)
# target_expr = parseTree("( f ( x , y ) * ( f x * f y ) )")
# # d1.semiAutoDerive([conditional, integrateOut, bayes, symmetry, associative])
# # d1.view()
# d1.autoDerive(target_expr, [conditional, conditional2, integrateOut, bayes, symmetry, associative])
