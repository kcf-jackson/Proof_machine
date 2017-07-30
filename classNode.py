class Node:
	def __init__(self, value = None, mathType = None, state = None):
		self.value = value
		self.mathType = mathType 
		self.state = state

class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.
    Modified to allow for trees to be constructed from other trees rather than always creating
    a new tree in the insertLeft or insertRight
    """
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):

        if isinstance(newNode, BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.leftChild is not None:
            t.left = self.leftChild

        self.leftChild = t

    def insertRight(self,newNode):
        if isinstance(newNode,BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.rightChild is not None:
            t.right = self.rightChild
        self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    # Right Child
    def getRightChild(self):
        return self.rightChild

    def getRightChildValue(self):
        return self.rightChild.getRootNodeValue()

    def getRightChildType(self):
        return self.rightChild.getRootNodeType()

    def getRightChildState(self):
        return self.rightChild.getRootNodeState()

    # Left Child
    def getLeftChild(self):
        return self.leftChild

    def getLeftChildValue(self):
        return self.leftChild.getRootNodeValue()

    def getLeftChildType(self):
        return self.leftChild.getRootNodeType()

    def getLeftChildState(self):
        return self.leftChild.getRootNodeState()

    # Root Node
    def setRootNode(self,obj):
        self.key = obj

    def getRootNode(self):
        return self.key

    def getRootNodeValue(self):
        return self.key.value

    def getRootNodeType(self):
        return self.key.mathType

    def getRootNodeState(self):
        return self.key.state

# if __name__ == '__main__':
#     t = BinaryTree(7)
#     t.insertLeft(3)
#     t.insertRight(9)
#     # inorder(t)
#     # import operator
#     x = BinaryTree('*')
#     x.insertLeft('+')
#     l = x.getLeftChild()
#     l.insertLeft(4)
#     l.insertRight(5)
#     x.insertRight(7)
#     # print(printexp(x))
#     # print(postordereval(x))
#     # print(height(x))