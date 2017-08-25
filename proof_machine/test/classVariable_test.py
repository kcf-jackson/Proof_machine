import os 
os.chdir('../')
exec(open('util.py').read())
exec(open('objClass//classVariable.py').read())
exec(open('objClass//classTree.py').read())

var = Variable("exp", 'function', ['scalar', 'real'], '\exp')
var.View()

globalVariables = Namespace()
globalVariables.addVariable(Variable('E', 'function'))
globalVariables.addVariable(Variable('gamma'))
globalVariables.addVariable(Variable('lambda', latex = '\lambda'))
globalVariables.addVariable(Variable('X', latex = 'X'))
globalVariables.View()

print(lookupPtype('lambda', globalVariables))

buildParseTree("E X", globalVariables).view()