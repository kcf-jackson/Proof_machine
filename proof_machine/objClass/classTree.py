from pythonds.basic.stack import Stack

class Node:
    def __init__(self, value = None, ptype = None, state = None):
        self.value = value
        self.ptype = ptype 
        self.state = state

    def __eq__(self, other):
        return self.value == other.value and self.ptype == other.ptype and self.state == other.state

    def view(self):
        print("Content: {}, Type: {}, State: {}".format(self.value, self.ptype, self.state))

class BinaryTree:
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
    def setRightChild(self, tree):
        self.rightChild = tree

    def getRightChild(self):
        return self.rightChild

    def getRightChildValue(self):
        return self.rightChild.getRootNodeValue()

    def getRightChildType(self):
        return self.rightChild.getRootNodeType()

    def getRightChildState(self):
        return self.rightChild.getRootNodeState()

    # Left Child
    def setLeftChild(self, tree):
        self.leftChild = tree
    
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
        return self.key.ptype

    def getRootNodeState(self):
        return self.key.state

    def view(self):
        print(treeToString(self))

    # def __add__(self, r):
    #     res = BinaryTree(Node("+", "operator"))
    #     res.insertLeft(tree)
    #     if getClass(r) in ["BinaryTree", "Node"]:
    #         res.insertRight(r)
    #     else
    #         res.insertRight(Node(r, 'symbol'))
    #     return res

    # def __radd__(self, l):
