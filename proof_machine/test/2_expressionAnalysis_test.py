from proof_machine.objClass import Namespace, treeToString
from proof_machine import parse, buildParseTree, tidyView
from proof_machine.treeMap import buildTreeMapping
import string

globalVariables = Namespace()
globalVariables.defineVariable('symbol', list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase))
globalVariables.defineVariable('function', 'int')
globalVariables.defineVariable('function', 'sum_i')
globalVariables.defineVariable('function', 'log')
globalVariables.defineVariable('symbol', 'X_i')
globalVariables.defineVariable('operator', [',', '|'])
globalVariables.defineVariable('symbol', 'dy')
globalVariables.modifyVariable('f', 'ptype', 'function')
globalVariables.modifyVariable('P', 'ptype', 'function')
globalVariables.modifyVariable('E', 'ptype', 'function')
globalVariables.addState("X", "random variable")
globalVariables.addState("Y", "random variable")
globalVariables.addState("Z", "random variable")
globalVariables.addState("a", "scaler")
globalVariables.addState("b", "scaler")
globalVariables.addState("c", "scaler")
globalVariables.View()


parse("E ( X * Y + Z )", globalVariables).View()
parse("E ( X ) + E ( Y )", globalVariables).View()


linear = buildTreeMapping("E ( X + Y )", "( E X + E Y )", globalVariables)
linear(parse("E ( Y + Z )", globalVariables)).View()

linearTwo = buildTreeMapping("E ( a * X + b * Y )", "( a * E ( X ) + b * E ( Y ) )", globalVariables)
print("Input 1")
parse("E ( a * X + b * Y ) ", globalVariables).View()
print("Input 2")
parse("( a * E ( X ) + b * E ( Y ) )", globalVariables).View()
print("Function result")
linearTwo(parse("E ( A * W + B * Z ) ", globalVariables), True).View()
linearTwo(parse("E ( a * X + b * Y ) ", globalVariables), True).View()
linearTwo(parse("E ( c * W + b * Y ) ", globalVariables), True).View()


tidyView(parse("E ( a * X + b * Y ) ", globalVariables), globalVariables)



# linearTwo(parse("E ( A * W + B * Z ) ", globalVariables), False).View()


# Density
# conditional = buildTreeMapping('f ( x , y )', '( f ( x | y ) * f y )', globalVariables)
# bayes = buildTreeMapping('f ( x | y )', '( f ( x , y ) / f y )', globalVariables)
# integrateOut = buildTreeMapping('f x', ' int ( f ( x , y ) * dy ) ', globalVariables)

# conditional(parse("f ( a , b )", globalVariables)).View()
# bayes(parse("f ( a | b )", globalVariables)).View()
# integrateOut(parse("f a", globalVariables)).View()


# # Inequality
# concavity = buildTreeMapping('( sum_i log X_i / n )', 'log ( sum_i X_i / n )', globalVariables)
# concavity(parse("( sum_i log X_i / n )", globalVariables)).View()


# parse("( sum_i log X_i / n )", globalVariables).View()
# parse("sum_i ( log ( X_i ) / n )", globalVariables).View()
# parse("sum_i ( log ( X_i / n ) )", globalVariables).View()

# parse('log ( sum_i X_i / n )', globalVariables).View()
# buildParseTree("( sum_i log X_i / n )", globalVariables).View()
# buildParseTree('log ( sum_i X_i / n )', globalVariables).View()
# # Equality
# expSumToProduct = buildTreeMapping('exp sum_i X_i', 'prod_i exp X_i')
# expProductToSum = buildTreeMapping('prod_i exp X_i', 'exp sum_i X_i')
# logProductToSum = buildTreeMapping('log prod_i X_i', 'sum_i log X_i')
# logSumToProduct = buildTreeMapping('sum_i log X_i', 'log prod_i X_i')
# independencePullOut = buildTreeMapping("E prod_i X_i", "prod_i E X_i")
# sumPushIn = buildTreeMapping('( t * sum_i X_i )', 'sum_i ( t * X_i )')
# sumPullOut = buildTreeMapping('sum_i ( t * X_i )', '( t * sum_i X_i )')


# # Analysis
# # 0 <= p <= 1
# quadraticBound = buildTreeMapping('( p * ( 1 - p ) )', '1 / 4')
# # Taylor's expansion
# taylor = buildTreeMapping('f x', '( f y + ( d_dx f y * ( x - y ) ) )')
# expTaylor = buildTreeMapping('exp x', '( ( ( ( 1 + x ) + ( ( x ^ 2 ) / 2 ) ) + ( ( x ^ 3 ) / 6 ) )')
# # Differentiation
# differentiate = buildTreeMapping('( g * h )', '( ( g * d_dx h ) + ( h * d_dx g ) )')



# print("Unit test for expressionToGenericMapping")
# print("Cauchy Schwarz's inequality")
# expressionToGenericMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 

# cauchySchwarz = buildTreeMapping('E ( X * Y )', 'sqrt ( E ( X ^ 2 ) * E ( Y ^ 2 ) )') 
# cauchySchwarz(parseTree('E ( X * Y )')).view()
# print("End\n")
# # see inequality.py
# # def cauchySchwarz(tree):
# # 	# Code mapping: 1200 to 1211220000
# # 	nodesList = treeToNodes(tree, '0011') + [Node("sqrt", 'function'), Node('^', 'operator'), Node('2', 'symbol')]
# # 	nodesDict = {1:5, 2:2, 3:1, 4:1, 5:6, 6:6, 7:3, 8:7, 9:4, 10:7}
# # 	return genericTreeMapping(nodesList, '1211220000', nodesDict)

# print("\nMarkov's inequality")
# expressionToGenericMapping('P ( X >= a )', '( E X / a )') 
# def markov(tree):
# 	nodesList = treeToNodes(tree, '0011') + [Node('/', 'operator'), Node("E", 'function')]
# 	nodesDict = {1: 5, 2: 6, 3: 4, 4: 3}
# 	return genericTreeMapping(nodesList, '2100', nodesDict)
# expr1 = parseTree('P ( X >= a )')
# markov(expr1).view()

# markov = buildTreeMapping('P ( X >= a )', '( E X / a )') 
# markov(expr1).view()
# print("End\n")


# print("\nInclusion/Exclusion principle")
# expressionToGenericMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )')
# def inclusionExclusion(tree):
# 	nodesList = treeToNodes(tree, '0011') + [Node('+', 'operator'), Node('-', 'operator'), Node("cap", 'operator')]
# 	nodesDict = {1: 6, 2: 5, 3: 1, 4: 1, 5: 1, 6: 7, 7: 3, 8: 4, 9: 3, 10: 4}
# 	return genericTreeMapping(nodesList, '2211120000', nodesDict)
# expr1 = parseTree('P ( A cup B )')
# inclusionExclusion(expr1).view()
# print("End\n")


# print("Unit test for buildTreeMapping")
# inclusionExclusion = buildTreeMapping('P ( A cup B )', '( ( P A + P B ) - P ( A cap B ) )', globalVariables)
# inclusionExclusion = buildTreeMapping('P ( A cup B )', 'P ( A ) + P ( B ) - P ( A cap B )', globalVariables)
# expr1 = parse('P ( A cup B )', globalVariables)
# expr1.View()
# inclusionExclusion(expr1).View()

# expr2 = parseTree('P ( A cup ( B cup C ) )')
# inclusionExclusion(expr2).view()
# print("End\n")