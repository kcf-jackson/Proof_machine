#==============================================================================
from pythonds.basic.stack import Stack
def baseConvert(decNum, base):
	digits = "0123456789ABCDEF"
	s = Stack()
	while decNum > 0:
		s.push(decNum % base)
		decNum = decNum // base
	cStr = ""
	while not s.isEmpty():
		cStr += digits[s.pop()]	
	return cStr

# def decRep(num, base):
# 	num = str(num)
# 	l = len(num)
# 	res = 0
# 	for i in range(l):
# 		res += int(num[-i-1]) * (base ** i)
# 	return res

# Unit test
# print(baseConvert(12, 3))
# print(decRep(110, 3))

def decRep(num, base):
	num = str(num)
	res = [int(num[-j-1]) * (base ** j) for j in range(len(num))]
	return sum(res)

# Unit test
# print(baseConvert(12, 3))
# print(decRep(110, 3))
