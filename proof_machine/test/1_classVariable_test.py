from proof_machine.objClass.classVariable import Variable, Namespace, lookupPtype

var = Variable("exp", 'function', ['scalar', 'real'], '\exp')
var.View()

globalVariables = Namespace()
globalVariables.addVariable(Variable('E', 'function'))
globalVariables.addVariable(Variable('gamma'))  # default is symbol
globalVariables.addVariable(Variable('lambda', latex = '\lambda'))
globalVariables.addVariable(Variable('X', latex = 'X'))
globalVariables.View()

print(lookupPtype('lambda', globalVariables))
