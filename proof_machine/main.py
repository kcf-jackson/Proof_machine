exec(open('setup.py').read())

print("\n=====Other tests=====")
expr = parseTree("( a + b )")
takeExp(expr).view()
takeLog(expr).view()
takeNegation(expr).view()
takeExpectation(expr).view()

pushInExp(takeExp(expr)).view()
pullOutExp(pushInExp(takeExp(expr))).view()

expr2 = parseTree("( a * b )")
takeLog(expr2).view()
pushInLog(takeLog(expr2)).view()
pullOutLog(pushInLog(takeLog(expr2))).view()

expr3 = parseTree("( ( a + b ) + c )")
forwardAssociative(expr3).view()
backwardAssociative(forwardAssociative(expr3)).view()

expr4 = parseTree("( ( a - b ) - c )")
forwardAssociative(expr4).view()
backwardAssociative(forwardAssociative(expr4)).view()

expr5 = parseTree("( ( a / b ) / c )")
expr5.view()
forwardAssociative(expr5).view()
backwardAssociative(forwardAssociative(expr5)).view()

expr6 = parseTree("E I ( X >= a )")
expr6.view()
functionalToMeasure(expr6).view()
measureToFunctional(functionalToMeasure(expr6)).view()

# print("Checking associative and distributive law...")
# associativeCase = ['++', '+-', '-+', '--', '**', '*/', '/*', '//']
# leftDistributiveCase = ['*+', '*-', '^+', '^-']
# rightDistributiveCase = ['+*', '-*', '', '', '', '', '']
# noCase = ['']
# arithmeticSymbol = ['+', '-', '*', '/', '^']
# for i in arithmeticSymbol:
# 	for j in arithmeticSymbol:
# 		if i + j in associativeCase:
# 			expr = parseTree("( c " + i + " ( a " +  j + " b ) )")
# 			print(treeToString(expr) + " = " + treeToString(backwardAssociative(expr)))
# 			expr2 = parseTree("( ( a " + i + " b ) " + j + " c )")
# 			print(treeToString(expr2) + " = " + treeToString(forwardAssociative(expr2)))
# 		else:
# 			# if i + j in leftDistributiveCase:
# 			expr = parseTree("( c " + i + " ( a " +  j + " b ) )")
# 			print(treeToString(expr) + " = " + treeToString(leftPushIn(expr)))
# 			# else:
# 			expr2 = parseTree("( ( a " + i + " b ) " + j + " c )")
# 			print(treeToString(expr2) + " = " + treeToString(rightPushIn(expr2)))
