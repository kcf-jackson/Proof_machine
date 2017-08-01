def getClass(obj):
	return obj.__class__.__name__

def isState(sym, state, variableState):
	return state in variableState[sym]
