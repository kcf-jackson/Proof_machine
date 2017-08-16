# Generate mapping for associative Dict
def getAssociativeMapping():
	import random
	import math
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
						print("('{:s}', '{:s}') : ('{:s}', '{:s}')".format(op1, op2, op3, op4))

# Generate mapping for distributive Dict
def getLeftDistributiveMapping():
	import random
	import math
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
				print("('{:s}', '{:s}')".format(op1, op2))

def getRightDistributiveMapping():
	import random
	import math
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
				print("('{:s}', '{:s}')".format(op1, op2))

print("Associative")
getAssociativeMapping()
print("Left distributive:")
getLeftDistributiveMapping()
print("Right distributive:")
getRightDistributiveMapping()
