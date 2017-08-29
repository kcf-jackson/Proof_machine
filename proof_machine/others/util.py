def getClass(obj):
	return obj.__class__.__name__

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def unique(list0):
	from orderedset import OrderedSet
	return list(OrderedSet(list0))

def map2(list1, list2, FUN):
	res = []
	for ind, i in enumerate(list1):
		res.append(FUN(list1[ind], list2[ind]))
	return sum(res, [])

def which(l0, element):
	res = []
	for ind, i in enumerate(l0):
		if i == element:
			res.append(ind)
	return res
	