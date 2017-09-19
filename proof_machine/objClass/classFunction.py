from proof_machine.treeMap.treeMapBuilder import buildTreeMapping

class FunctionSpace:
	def __init__(self, namespace):
		self.functionList = {}
		self.namespace = namespace

	def addFunction(self, example):
		# this function takes a list of form: [input, output, function name] or [input, output, [name_1, name2]]
		inputStr = example[0]
		outputStr = example[1]
		nameStr = example[2]
		if len(nameStr) == 2:
			self.functionList[nameStr[0]] = buildTreeMapping(inputStr, outputStr, self.namespace)
			self.functionList[nameStr[1]] = buildTreeMapping(outputStr, inputStr, self.namespace)
			print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(nameStr[0], inputStr, outputStr))
			print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(nameStr[1], outputStr, inputStr))
		else:
			self.functionList[nameStr] = buildTreeMapping(inputStr, outputStr, self.namespace)
			print("Added function:  {:^26} \t that maps {:^35} \t to {:^40}".format(nameStr, inputStr, outputStr))

	def addListOfFunctions(self, exampleList):
		[self.addFunction(x) for x in exampleList]
