import os 
os.chdir('../')
exec(open('load.py').read())

expr1 = parseTree("P ( A cup B )")
expr2 = parseTree("( P A + P B )")
print(treeDiff(expr1, expr1))
print(treeDiff(expr1, expr2))
print(treeDiff(expr2, expr2))
