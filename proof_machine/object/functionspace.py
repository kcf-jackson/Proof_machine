from proof_machine.treeMap.treeMapBuilder import buildTreeMapping

class FunctionSpace:
	"""keeps track of the mappings between trees.

	Attributes:
		functionList, namespace
	"""
	def __init__(self, namespace):
		self.functionList = {}
		self.namespace = namespace

	def addFunction(self, example):
		""" adds function to the functionList

		The function takes a list of form [input, output, function name] or [input, output, [name_1, name2]].
		In the former case, it adds a tree mapping (from input to output) with the name 'function name';
		in the latter case, it add two mappings, one with the usual direction and one with the reverse direction (of input, output).
		"""
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
		""" add a list of functinos to the functionList. """
		[self.addFunction(x) for x in exampleList]
