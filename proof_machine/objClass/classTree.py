from pythonds.basic.stack import Stack

class Node:
	def __init__(self, value = None, mathType = None, state = None):
		self.value = value
		self.mathType = mathType 
		self.state = state

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
        return self.key.mathType

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

def buildParseTree(fpexp, unaryOpList, binaryOpList):
    tokenList = fpexp.split()   # Expression to be parsed
    exprTree = BinaryTree('')   # Expression Tree
    parentStack = Stack()       # Keep track of the parent node
    parentStack.push(exprTree)  

    parenthesesList = unaryOpList[0:6]
    currentTree = exprTree
    for ind, i in enumerate(tokenList):
        if i in unaryOpList:
            if i in parenthesesList[0:3]:
            # if it is an open parentheses
                currentTree.setRootNode(Node(i, 'parentheses')) 
                currentTree.insertLeft('')
                parentStack.push(currentTree)
                currentTree = currentTree.getLeftChild()
            elif i in unaryFunctionList:
            # if it is an unary function
                currentTree.setRootNode(Node(i, 'function'))
                currentTree.insertLeft('')
                parentStack.push(currentTree)
                currentTree = currentTree.getLeftChild()        
            elif i in parenthesesList[3:6]:
            # if it is a close parentheses
                currentTree = parentStack.pop()
                if currentTree.getRootNodeType() == 'function':
                    currentTree = parentStack.pop()
        elif i in binaryOpList:
            # if it is an binary operator
            currentTree.setRootNode(Node(i, 'operator'))
            currentTree.insertRight('')
            parentStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i not in binaryOpList and i not in parenthesesList[3:6]:
            # if it is a constant or symbol (leaf)
            currentTree.setRootNode(Node(i, 'symbol'))
            currentTree = parentStack.pop()  # move up one level
            if currentTree.getRootNodeType() == 'function':
                    currentTree = parentStack.pop()
        else:
            raise ValueError
    return exprTree

def treeToString(tree):
    sVal = ""
    if tree.getRootNodeType() == 'function':
        return str(tree.getRootNodeValue()) + ' ' + treeToString(tree.getLeftChild())
    elif tree.getRootNodeType() == 'symbol':
        return str(tree.getRootNodeValue())
    elif tree.getRootNodeType() == 'operator':
        return '( ' + treeToString(tree.getLeftChild()) + ' ' + str(tree.getRootNodeValue()) + ' ' + treeToString(tree.getRightChild())+ ' )'
    elif tree.getRootNodeType() == 'parentheses':
        return '( ' + treeToString(tree.getLeftChild()) + ' )'

def printFullTree(tree, level = 0):
  print("  " * level + tree.getRootNodeValue() + ' ' + tree.getRootNodeType())
  if tree.getLeftChild() != None:
    printFullTree(tree.getLeftChild(), level + 1)
  if tree.getRightChild() != None:
    printFullTree(tree.getRightChild(), level + 1)
