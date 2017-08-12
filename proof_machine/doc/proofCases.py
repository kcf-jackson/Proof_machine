#==============================================================================
# Main
#==============================================================================
import os 
os.chdir('../')
exec(open('load.py').read())

# Proof of Markov's inequality
print("Markov's inequality")
lhs = parseTree("( a * I ( X >= a ) )")
op = "<="
rhs = parseTree("X")
masterEq = Equation(lhs, op, rhs)
masterEq.view()

masterEq.applyToBoth(div_X, Node('a', 'symbol'))
masterEq.applyToLeft(simplifyDiv)
masterEq.applyToBoth(takeExpectation)
masterEq.applyToLeft(functionalToMeasure)
