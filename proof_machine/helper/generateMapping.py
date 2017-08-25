# Generate mapping for associative Dict
def getAssociativeMapping():
	import random
	import math
	res = []
	sym = ['+', '-', '*', '/']
	for op1 in sym:
		for op2 in sym:
			for op3 in sym:
				for op4 in sym:
					a = str(round(random.uniform(50, 100), 3))
					b = str(round(random.uniform(50, 100), 3))
					c = str(round(random.uniform(50, 100), 3))
					expr1 = "".join(['(', a, op1, b, ')', op2, c])
					expr2 = "".join([a, op3, '(', b, op4, c, ')'])
					if math.isclose(eval(expr1), eval(expr2)):
						# print("".join([expr1, '=', expr2]))
						resExpr1 = " ".join(['( (', 'a', op1, 'b', ')', op2, 'c )'])
						resExpr2 = " ".join(['( a', op3, '(', 'b', op4, 'c', ') )'])
						res.append([resExpr1, resExpr2])
						# print("('{:s}', '{:s}') : ('{:s}', '{:s}')".format(op1, op2, op3, op4))
	res = res + list(map(lambda x: x[::-1], res))
	print("Generated Arithmetric - Associative law - " + str(len(res)) + " examples.")
	return res

# Generate mapping for distributive Dict
def getLeftDistributiveMapping():
	import random
	import math
	res = []
	sym = ['+', '-', '*', '/']
	for op1 in sym:
		for op2 in sym:
			a = str(round(random.uniform(50, 100), 3))
			b = str(round(random.uniform(50, 100), 3))
			c = str(round(random.uniform(50, 100), 3))
			expr1 = "".join([a, op1, '(', b, op2, c, ')'])
			expr2 = "".join(['(', a, op1, b, ')', op2, '(', a, op1, c, ')'])
			if math.isclose(eval(expr1), eval(expr2)):
				# print("".join([expr1, '=', expr2]))
				# print("('{:s}', '{:s}')".format(op1, op2))
				resExpr1 = " ".join(['( a', op1, '(', 'b', op2, 'c', ') )'])
				resExpr2 = " ".join(['( ( a ', op1, 'b )', op2, '( a', op1, 'c ) )'])
				res.append([resExpr1, resExpr2])
	print("Generated Arithmetric - Left distributive law - " + str(len(res)) + " examples.")
	return res

def getRightDistributiveMapping():
	import random
	import math
	res = []
	sym = ['+', '-', '*', '/']
	for op1 in sym:
		for op2 in sym:
			a = str(round(random.uniform(50, 100), 3))
			b = str(round(random.uniform(50, 100), 3))
			c = str(round(random.uniform(50, 100), 3))
			expr1 = "".join(['(', a, op1, b, ')', op2, c])
			expr2 = "".join(['(', a, op2, c, ')', op1, '(', b, op2, c, ')'])
			if math.isclose(eval(expr1), eval(expr2)):
				# print("".join([expr1, '=', expr2]))
				# print("('{:s}', '{:s}')".format(op1, op2))
				resExpr1 = " ".join(['( (', 'a', op1, 'b', ')', op2, 'c )'])
				resExpr2 = " ".join(['( (', 'a', op2, 'c', ')', op1, '(', 'b', op2, 'c', ')'])
				res.append([resExpr1, resExpr2])
	print("Generated Arithmetric - Right distributive law - " + str(len(res)) + " examples.")
	return res

print("Associative")
[print(x) for x in getAssociativeMapping()]
print("Left distributive:")
[print(x) for x in getLeftDistributiveMapping()]
print("Right distributive:")
[print(x) for x in getRightDistributiveMapping()]


