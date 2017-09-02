from pythonds.basic.stack import Stack
from proof_machine.others import precTable, isfloat
from proof_machine.objClass import lookupPtype, BinaryTree, Node, lookupState

def buildParseTree(fpexp, namespace):
    tokenList = fpexp.split()   # Expression to be parsed
    exprTree = BinaryTree('')   # Expression Tree
    parentStack = Stack()       # Keep track of the parent node
    parentStack.push(exprTree)  

    currentTree = exprTree
    for ind, i in enumerate(tokenList):
        varParseType = lookupPtype(i, namespace)
        if varParseType == 'undefined':
            # Add the symbol to global namespace if it's a numeric
            if isfloat(i):
                namespace.defineVariable('symbol', i)
                varParseType = lookupPtype(i, namespace)
        # Add nodes and move down/right the tree
        if varParseType == 'function':
            currentTree.setRootNode(Node(i, 'function', lookupState(i, namespace)))
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()        
        elif varParseType == 'operator':
            currentTree.setRootNode(Node(i, 'operator', lookupState(i, namespace)))
            currentTree.insertRight('')
            parentStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i in ['{', '[', '(']: 
            currentTree.setRootNode(Node(i, 'parentheses', lookupState(i, namespace))) 
            currentTree.insertLeft('')
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        # Add nodes and move up the tree
        elif varParseType == 'symbol':
            currentTree.setRootNode(Node(i, 'symbol', lookupState(i, namespace)))
            currentTree = parentStack.pop()  # move up one level
            while currentTree.getRootNodeType() == 'function' and not parentStack.isEmpty():
                    currentTree = parentStack.pop()    
        elif i in [')', ']', '}']:
            currentTree = parentStack.pop()
            while currentTree.getRootNodeType() == 'function' and not parentStack.isEmpty():
                currentTree = parentStack.pop()
        else:
            raise ValueError("Variable " + i + " has wrong parse type: "+ varParseType + ". Must be 'function', 'operator', 'symbol' or 'parentheses'.")
            
    return exprTree

def infixToPostfix(expr, namespace):
    prec = precTable()
    opStack = Stack()
    postfixList = []
    tokenList = expr.split()

    for token in tokenList:
        # symbol
        tokenPtype = lookupPtype(token, namespace)
        if tokenPtype == 'symbol':
            postfixList.append(token)
        # parentheses
        elif token == '(' or tokenPtype == 'function':
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

def postfixToInfix(expr, namespace):
    prec = precTable()
    symbolStack = Stack()
    infixStr = ''
    tokenList = expr.split()

    for token in tokenList:
        tokenPtype = lookupPtype(token, namespace)
        if tokenPtype == 'symbol':
            symbolStack.push(token)
        elif tokenPtype == 'operator':
            right = symbolStack.pop()
            left = symbolStack.pop()
            symbolStack.push(" ".join(['(', left, token, right, ')']))
        elif tokenPtype == 'function':
            center = symbolStack.pop()
            # symbolStack.push(" ".join([token, '(', center, ')']))
            symbolStack.push(" ".join([token, center]))
        else:
            raise ValueError(token + " has the wrong parse type.")

    if symbolStack.size() == 1:
        return symbolStack.pop()
    else:
        raise ValueError("Final outcome doesn't have size 1.")

def postfixToInfixSimplified(expr, namespace):
    prec = precTable()
    symbolStack = Stack()
    precStack = Stack()
    infixStr = ''
    tokenList = expr.split()

    for token in tokenList:
        tokenPtype = lookupPtype(token, namespace)
        if tokenPtype == 'symbol':
            symbolStack.push(token)
            precStack.push(100)
        elif tokenPtype == 'operator':
            right = symbolStack.pop()
            left = symbolStack.pop()
            
            tokenPrec = prec[token]
            rightPrec = precStack.pop()
            leftPrec = precStack.pop()
            if leftPrec < tokenPrec:
                left = '( ' + left + ' )'    
            if rightPrec <= tokenPrec:
                right = '( ' + right + ' )'  
            precStack.push(prec[token])
            
            symbolStack.push(" ".join([left, token, right]))
        elif tokenPtype == 'function':
            if token not in prec:
                prec[token] = 0
            precStack.pop()
            precStack.push(100)
            center = symbolStack.pop()
            symbolStack.push(" ".join([token, '(', center, ')']))
        else:
            raise ValueError(token + " has the wrong parse type.")

    if symbolStack.size() == 1:
        return symbolStack.pop()
    else:
        raise ValueError("Final outcome doesn't have size 1.")

def parse(expr, globalVariables):
    postfixExpr = infixToPostfix(expr, globalVariables)
    fullInfixExpr = postfixToInfix(postfixExpr, globalVariables)
    return buildParseTree(fullInfixExpr, globalVariables)
