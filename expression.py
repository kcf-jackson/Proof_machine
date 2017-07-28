def leq(expr1, expr2):
	return str(expr1) + "<=" + str(expr2)

def geq(expr1, expr2):
	return str(expr1) + ">=" + str(expr2)

def eq(expr1, expr2):
	return str(expr1) + "=" + str(expr2)

def l(expr1, expr2):
	return str(expr1) + "<" + str(expr2)

def g(expr1, expr2):
	return str(expr1) + ">" + str(expr2)

def View(expr):
	print("".join(expr))

# Unit test
# expr1 = ["f1" , "<=", "f2"]
# View(expr1)
# View(takeExpectation(expr1))

def expectationToProbability(expr):
	parseStart = False
	parseChar = ''
	for char in expr:
		if parseStart:
			parseChar += char
		if char == '{':
			parseStart = True
		elif char == '}':
			parseStart = False
	return "P(" + parseChar[:-1] + ")"

def probabilityToExpectation(expr):
	parseStart = False
	parseChar = ''
	for char in expr:
		if parseStart:
			parseChar += char
		if char == '(':
			parseStart = True
		elif char == ')':
			parseStart = False
	return "E[I_{" + parseChar[:-1] + "}]"

# Unit test
# print(expectationToProbability("E[I_{X>=a}]"))
# print(probabilityToExpectation("P(X>=a)"))

