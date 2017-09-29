print("Unit test: Object class Namespace")
from proof_machine.objClass import Namespace
import string
globalVariables = Namespace()
globalVariables.defineVariable('symbol', list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase))
globalVariables.modifyVariable('f', 'ptype', 'function')
globalVariables.modifyVariable('P', 'ptype', 'function')
globalVariables.View()


print("Unit test: Conversion between infix, postfix and simplified postfix")
def test(expr, globalVariables):
	from proof_machine import infixToPostfix, postfixToInfix, postfixToInfixSimplified
	a = infixToPostfix(expr, globalVariables)
	b = postfixToInfix(a, globalVariables)
	c = postfixToInfixSimplified(a, globalVariables)
	print("\n".join([expr, a, b, c, "\n"]))

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

test("f ( A * B )", globalVariables)
