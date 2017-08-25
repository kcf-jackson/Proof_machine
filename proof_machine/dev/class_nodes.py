# Constant/Symbols nodes should be leafs
# Operators nodes should be unary, binary or n-ary. The classification is based on how many leafs they have.
# - Parenthesis comes in pairs and their value is empty.
class Node:
	def __init__(self, value = None, ptype = None, state = None):
		self.value = value
		self.ptype = ptype 
		self.state = state

	def setRootValue(self, obj):
		self.value = obj

	def getRootValue(self):
		return self.value

	def setType(self, obj):
		self.ptype = obj

	def getType(self):
		return self.ptype

	def setState(self, obj):
		self.state = obj

	def getState(self):
		return self.state


class Leaf(Node):
	def __init__(self):
		Node.__init__(self)

		
class UnaryOp(Node):
	def __init__(self, rootObj):
		Node.__init__(self)
		self.setRootValue(rootObj)
		self.child = None


class BinaryOp:
	def __init__(self, rootObj):
		Node.__init__(self)
		Node.setRootValue(self, rootObj)
		self.leftChild = None
		self.rightChild = None

	def print(self):
		print(str(self.leftChild) + str(Node.getRootValue(self)) + str(self.rightChild))


class NaryOp:
	def __init__(self, rootObj):
		Node.__init__(self)
		Node.setRootValue(rootObj)
		self.children = []


class Tree:
	def __init__(self, rootObj):
		Node.__init__(self)
		Node.setRootValue(rootObj)
		
a = "3 + 4"
op = BinaryOp("+")
op.leftChild = '3'
op.rightChild = '4'
op.print()

# a = Tree()
	# def insertLeft(self, newNode):
	# 	if self.leftChild == None:
	# 		self.leftChild = BinaryTree(newNode)
	# 	else:
	# 		t = BinaryTree(newNode)
	# 		t.leftChild = self.leftChild
	# 		self.leftChild = t

	# def insertRight(self, newNode):
	# 	if self.rightChild == None:
	# 		self.rightChild = BinaryTree(newNode)
	# 	else:
	# 		t = BinaryTree(newNode)
	# 		t.rightChild = self.rightChild
	# 		self.rightChild = t

	# def getRightChild(self):
	#     return self.rightChild

	# def getLeftChild(self):
	#     return self.leftChild

	# def setRootVal(self,obj):
	#     self.key = obj

	# def getRootVal(self):
	#     return self.key

 