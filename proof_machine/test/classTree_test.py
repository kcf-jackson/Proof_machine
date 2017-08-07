import os 
os.chdir('../')
exec(open('load.py').read())

print("Unit test for basic tree parsing: buildParseTree")
pt = buildParseTree("( ( ( 10 + 5 ) * 3 ) <= 50 )", unaryOpList, binaryOpList)
print(treeToString(pt))
