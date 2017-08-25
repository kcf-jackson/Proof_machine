def getClass(obj):
	return obj.__class__.__name__

def ifelse(bool0, res1, res2):
	if bool0:
		return res1
	return res2

def unique(list0):
	from orderedset import OrderedSet
	return list(OrderedSet(list0))

def map2(list1, list2, FUN):
	res = []
	for ind, i in enumerate(list1):
		res.append(FUN(list1[ind], list2[ind]))
	return sum(res, [])
