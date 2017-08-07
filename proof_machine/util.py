def getClass(obj):
	return obj.__class__.__name__

def isState(sym, state, variableState):
	return state in variableState[sym]

from functools import partial
isConstant = partial(isState, state = "constant")
isFunction = partial(isState, state = "function")
isRandomVariable = partial(isState, state = "random variable")

def isSymbol(tree):
	return tree.getRootNodeType() == 'symbol'

def isVariable(sym, variableState):
	return sym in variableState
