import os
os.chdir("../")

# exec(open('factory//basicTreePattern.py').read())
# exec(open('factory//genericTreePattern.py').read())
# exec(open('factory//expressionAnalysis.py').read())
exec(open('factory//treeEncoding.py').read())
# exec(open('factory//treeEquality.py').read())
exec(open('objClass//classTree.py').read())
# exec(open('objClass//classDerivation.py').read())
exec(open('objClass//classVariable.py').read())
exec(open('treeParser.py').read())
exec(open('util.py').read())

globalVariables = Namespace()
globalVariables.addVariable(Variable('f', 'function'))
globalVariables.View()

print(infixToPostfix("A * B + C * D", namespace = globalVariables))
print(lookupPtype('(', globalVariables))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )", namespace = globalVariables))

print(infixToPostfix("f ( f ( A * B ) + C ) * f ( D )", namespace = globalVariables))
print(infixToPostfix("( ( A + B ) + C )", namespace = globalVariables))

print(infixToPostfix("A + B + C", namespace = globalVariables))
print(infixToPostfix("( A + B + C )", namespace = globalVariables))
