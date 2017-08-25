def buildParseTree(fpexp, namespace):
    tokenList = fpexp.split()   # Expression to be parsed
    exprTree = BinaryTree('')   # Expression Tree
    parentStack = Stack()       # Keep track of the parent node
    parentStack.push(exprTree)  

    currentTree = exprTree
    for ind, i in enumerate(tokenList):
        varParseType = lookupPtype(i, namespace)
        # Add nodes and move down/right the tree
        if varParseType == 'function':
            currentTree.setRootNode(Node(i, 'function'))
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()        
        elif varParseType == 'operator':
            currentTree.setRootNode(Node(i, 'operator'))
            currentTree.insertRight('')
            parentStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i in ['{', '[', '(']: 
            currentTree.setRootNode(Node(i, 'parentheses')) 
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # Add nodes and move up the tree
        elif varParseType == 'symbol':
            currentTree.setRootNode(Node(i, 'symbol'))
            currentTree = parentStack.pop()  # move up one level
            while currentTree.getRootNodeType() == 'function' and not parentStack.isEmpty():
                    currentTree = parentStack.pop()    
        elif i in [')', ']', '}']:
            currentTree = parentStack.pop()
            while currentTree.getRootNodeType() == 'function' and not parentStack.isEmpty():
                currentTree = parentStack.pop()
        else:
            raise ValueError("Wrong parse type for variable " + i + ". Must be 'function', 'operator', 'symbol' or 'parentheses'.")
            
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

def infixToPostfix(infixexpr, namespace):
    # note that functions" have higher precedence than all the operators.
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, '<': 1, '>': 1, '<=': 1, '>=': 1, '=': 1, "(": 0}
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        # symbol
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # parentheses
        elif token == '(' or lookupPtype(token, namespace) == 'function':
            opStack.push(token)
            if token not in prec:
                prec[token] = 0
        elif token == ')':
            topToken = opStack.pop()
            # pop untils you see a open parentheses
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
            if not opStack.isEmpty() and lookupPtype(opStack.peek(), namespace) == 'function':
                topToken = opStack.pop()
                postfixList.append(topToken)
        # operator
        else:
            while (not opStack.isEmpty() and prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# def postfixToInfix(expr):

# def combineTwoTrees(tree1, tree2, node):
#     res = BinaryTree(node)
#     res.insertLeft(tree1)
#     res.insertRight(tree2)
#     return res

# Helper functions
def lookupPtype(varName, namespace):
    res = namespace.findVariable(varName)
    return res.ptype if res else ''
