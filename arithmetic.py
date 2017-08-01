# This file contains operations on Trees.
from functools import partial

# Univariate function mapping (Add one function node on top)
def ApplyFunctionToTree(tree, fun):
	return addOneNodeOnTop(tree, Node(fun, 'function'))

takeExp = partial(ApplyFunctionToTree, fun = 'exp')
takeLog = partial(ApplyFunctionToTree, fun = 'log')
takeExpectation = partial(ApplyFunctionToTree, fun = 'E')
takeNegation = partial(ApplyFunctionToTree, fun = '-')


# Arithmetic on trees (Add one operator node on top)
def Tree_Operator_X(tree, x, op):
	res = BinaryTree(Node(op, "operator"))
	res.insertLeft(tree)
	res.insertRight(x)
	return res

def X_Operator_Tree(tree, x, op):
	res = BinaryTree(Node(op, "operator"))
	res.insertLeft(x)
	res.insertRight(tree)
	return res

add_X = partial(Tree_Operator_X, op = '+')
sub_X = partial(Tree_Operator_X, op = '-')
mul_X = partial(Tree_Operator_X, op = '*')
div_X = partial(Tree_Operator_X, op = '/')
pow_X = partial(Tree_Operator_X, op = '^')

X_add = partial(X_Operator_Tree, op = '+')
X_sub = partial(X_Operator_Tree, op = '-')
X_mul = partial(X_Operator_Tree, op = '*')
X_div = partial(X_Operator_Tree, op = '/')
X_pow = partial(X_Operator_Tree, op = '^')
