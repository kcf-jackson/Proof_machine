import string
import os
os.chdir("../")

exec(open('others//initialisation.py').read())
exec(open('objClass//classTree.py').read())
exec(open('objClass//classVariable.py').read())
exec(open('treeParser.py').read())

globalVariables = Namespace()
globalVariables.defineVariable('symbol', list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase))
globalVariables.modifyVariable('f', 'ptype', 'function')
globalVariables.modifyVariable('P', 'ptype', 'function')
globalVariables.View()


print("Unit test: Conversion between infix, postfix and simplified postfix")
def test(expr, globalVariables):
	a = infixToPostfix(expr, globalVariables)
	b = postfixToInfix(a, globalVariables)
	c = postfixToInfixSimplified(a, globalVariables)
	print(expr)
	print(a)
	print(b)
	print(c)
	print()

test("A * B + C * D", globalVariables)
test("( A + B ) * C - ( D - E ) * ( F + G )", globalVariables)
test("f ( f ( A * B ) + C ) * f ( D )", globalVariables)

test("( ( A + B ) + C )", globalVariables)
test("A + B + C", globalVariables)
test("( A + B + C )", globalVariables)
test("( A + ( B + ( C + D ) ) )", globalVariables)
test("A + ( B +  C ) + D", globalVariables)

test("A - B - C", globalVariables)
test("( ( A - B ) - C )", globalVariables)
test("( A - ( B - ( C - D ) ) )", globalVariables)
test("A - ( B -  C ) - D", globalVariables)

test("P ( A ) + P ( B )", globalVariables)
test("P ( A cup B cap C )", globalVariables)
