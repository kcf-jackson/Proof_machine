import os 
os.chdir('../')
exec(open('load.py').read())

print("Unit test for div_X, simplifyDiv")
pt = buildParseTree("( a * b )", unaryOpList, binaryOpList)
print(treeToString(pt))

pt = div_X(pt, Node('b', 'symbol'))
print(treeToString(pt) + " [div_X] ")

pt = simplifyDiv(pt)
print("" + treeToString(pt) + " [simplifyDiv] ")
