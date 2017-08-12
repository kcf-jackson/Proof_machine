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
