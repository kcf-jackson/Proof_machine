import string
import os
os.chdir("../")

exec(open('others//initialisation.py').read())
exec(open('others//util.py').read())
exec(open('objClass//classTree.py').read())
exec(open('objClass//classVariable.py').read())

exec(open('treeParser.py').read())

globalVariables = Namespace()
globalVariables.defineVariable('symbol', list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase))

print("Unit test for basic tree parsing: buildParseTree")
pt = buildParseTree("( ( ( 82 + 5 ) * 3 ) >= 5 )", globalVariables)
print(treeToString(pt))
