from proof_machine.objClass import Namespace
from proof_machine import buildParseTree

print("Unit test for basic tree parsing: buildParseTree")
globalVariables = Namespace()
buildParseTree("( ( ( 82 + 5 ) * 3 ) >= 5 )", globalVariables).View()
