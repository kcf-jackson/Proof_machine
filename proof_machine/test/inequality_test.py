import os 
os.chdir('../')
exec(open('load.py').read())

print("Cauchy Schwarz's inequality")
expr = parseTree("E ( X * Y )")
expr.view()
cauchySchwarz(expr).view()

expr = parseTree("E ( X * I ( X <= A ) )")
expr.view()
cauchySchwarz(expr).view()
print("End\n")


print("\nMarkov's inequality")
expr1 = parseTree('P ( X >= a )')
markov(expr1).view()
print("End\n")


print("\nInclusion/Exclusion principle")
expr1 = parseTree('P ( A cup B )')
inclusionExclusion(expr1).view()
print("End\n")


print("\nChernoff bound")
expr1 = parseTree('P ( abs ( sum_i X_i ) >= ( k * sigma ) )')
chernoff(expr1).view()
print("End\n")


print("\nSum to product for exponential functions")
expr1 = parseTree('exp sum_i X_i')
expSumToProduct(expr1).view()
expProductToSum(expSumToProduct(expr1)).view()

expr1 = parseTree('exp sum_i ( a_i * Y_i )')
expSumToProduct(expr1).view()
expProductToSum(expSumToProduct(expr1)).view()


print("\nJensen's inequality")
expr1 = parseTree('log E sum_i X_i')
jensen(expr1).view()


# Lemma 2.6 of concentration inequalities
print("\nUnit test for sumPushIn, expSumToProduct, independencePull, logProductToSum")
d1 = Derivation(parseTree("( log E exp ( t * S ) / n )"))
d1.replace('S', 'sum_i X_i')
d1.substitute('( t * sum_i X_i )', sumPushIn)
d1.substitute('exp sum_i ( t * X_i )', expSumToProduct)
d1.substitute('E prod_i exp ( t * X_i )', independencePullOut)
d1.substitute('log prod_i E exp ( t * X_i )', logProductToSum)
d1.derive(concavity)
d1.view()
print("QED\n")


print("Unit test for autoDerive")
d1 = Derivation(parseTree("( log E exp ( t * sum_i X_i ) / n )"))
funList = [sumPushIn, expSumToProduct, independencePullOut, logProductToSum, concavity]
nameList = ['sumPushIn', 'expSumToProduct', 'independencePull', 'logProductToSum', 'concavity']
d1.blindDerive(funList, 6, nameList)
d1.view()
print("QED\n")


# expr = "( log E exp ( t * sum_i X_i ) / n )"
# funList = [sumPushIn, expSumToProduct, independencePull, logProductToSum]
# treeList = getAllParents(parseTree(expr))
# for subTree in treeList:
# 	for fun in funList:
# 		transformedTree = fun(subTree)
# 		if transformedTree != subTree:
# 			print(treeToString(subTree) + ' -> ' + treeToString(transformedTree))
			
