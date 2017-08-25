import os 
os.chdir('../')
exec(open('load.py').read())

expr = parseTree('f ( x , y )')
conditional(expr).view()

expr = parseTree('f ( ( x , y ) , z )')
conditional(expr).view()

expr = parseTree('E ( X * Y )')
cauchySchwarz(expr).view()

expr = parseTree('E ( ( a * X ) + ( b * Y ) )')
[x.view() for x in treeToNodes(expr)]
expectationLinearity(expr).view()

expr = parseTree('E ( ( Z * X ) + ( W * Y ) )')
expectationLinearity(expr).view()
