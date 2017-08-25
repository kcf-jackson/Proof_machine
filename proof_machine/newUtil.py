def buildTypeDict(full_list, parenthesesList, functionList, operatorList, variableList):
	typeDict = {}
	for i in full_list:
		if i in parenthesesList:
			typeDict[i] = 'parentheses'
		elif i in functionList:
			typeDict[i] = 'function'
		elif i in operatorList:
			typeDict[i] = 'operator'
		# elif i in constantList:
		# 	typeDict[i] = 'constant'
		# elif i in rvList:
		# 	typeDict[i] = 'random variable'
		else:
			typeDict[i] = 'symbol'
	return typeDict

def whatType(sym, typeDict):
	return typeDict[sym]


# def isState(sym, state, variableState):
# 	return state in variableState[sym]

# from functools import partial
# isConstant = partial(isState, state = "constant")
# isFunction = partial(isState, state = "function")
# isRandomVariable = partial(isState, state = "random variable")

# def isSymbol(tree):
# 	return tree.getRootNodeType() == 'symbol'

# def isVariable(sym, variableState):
# 	return sym in variableState
