# Unit test for buildParseTree
if __name__ == '__main__':
  exec(open('classEquation.py').read())
  exec(open('classTree.py').read())
  exec(open('patternConversion.py').read())
  exec(open('arithmetic.py').read())
  exec(open('factoriseAndExpand.py').read())
  exec(open('simplify.py').read())
  exec(open('util.py').read())
  parenthesesList = ['{', '[', '(', ')', ']', '}']
  unaryFunctionList = ['E', 'I', 'P', 'exp', 'log']
  unaryOpList = parenthesesList + unaryFunctionList
  binaryOpList = ['+', '-', '*', '/', '^', '<', '>', '<=', '>=', '=', '=>']
  opList = unaryOpList + binaryOpList
  variableState = {'a': ['constant'], 'b': ['constant'], 'X': ['random variable'], 'Y': ['random variable'], 'I': ['function']}

  parseTree = partial(buildParseTree, unaryOpList = unaryOpList, binaryOpList = binaryOpList)

  print("Unit test for basic tree parsing: buildParseTree")
  pt = buildParseTree("( ( ( 10 + 5 ) * 3 ) <= 50 )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  print("Unit test for div_X, simplifyDiv")
  pt = buildParseTree("( a * b )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = div_X(pt, Node('b', 'symbol'))
  print(treeToString(pt) + " [div_X] ")

  pt = simplifyDiv(pt)
  print("" + treeToString(pt) + " [simplifyDiv] ")

  print("Unit test for takeExpectation, pushInExpectation, pullOutExpectation")
  pt = buildParseTree("( a + b )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = takeExpectation(pt)
  print(treeToString(pt) + " " + "[Take expectation]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Push in]")

  pt = pullOutExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Pull out]")

  pt = buildParseTree("( X * Y )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = takeExpectation(pt)
  print(treeToString(pt) + " " + "[Take expectation]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Push in]")

  pt = pullOutExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Pull out]")

  pt = buildParseTree("( a * Y )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = takeExpectation(pt)
  print(treeToString(pt) + " " + "[Take expectation]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Push in]")

  pt = pullOutExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Pull out]")

  pt = buildParseTree("( X * b )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = takeExpectation(pt)
  print(treeToString(pt) + " " + "[Take expectation]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Push in]")

  pt = pullOutExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Pull out]")

  pt = buildParseTree("( ( a * X ) + ( b * Y ) )", unaryOpList, binaryOpList)
  print(treeToString(pt))

  pt = takeExpectation(pt)
  print(treeToString(pt) + " " + "[Take expectation]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Push in]")

  pt = pushInExpectation(pt, variableState)
  print(treeToString(pt) + " " + "[Pull out]")

  # Important test case: Markov's inequality 
  print("Markov's inequality")
  pt = buildParseTree("( a * I ( X >= a ) )", unaryOpList, binaryOpList)
  pt2 = buildParseTree(" X ", unaryOpList, binaryOpList)
  print( treeToString(pt) + " <= " + treeToString(pt2) )

  pt = div_X(pt, Node('a', 'symbol'))
  pt2 = div_X(pt2, Node('a', 'symbol'))
  print( treeToString(pt) + " <= " + treeToString(pt2) )

  pt = simplifyDiv(pt)
  print( treeToString(pt) + " <= " + treeToString(pt2) )

  pt = takeExpectation(pt)
  pt2 = takeExpectation(pt2)
  print( treeToString(pt) + " <= " + treeToString(pt2) )

  pt = functionalToMeasure(pt)
  print( treeToString(pt) + " <= " + treeToString(pt2) )
  # print( treeToString(pt) + " <= " + treeToString(pt2) )

  print("Unit Testing for leftPushIn, leftPushOut, rightPushIn, rightPushOut")
  expr = parseTree( "( c * ( a + b ) )")
  print(' = '.join(map(treeToString, [expr, leftPushIn(expr), leftPullOut(leftPushIn(expr))])))

  expr = parseTree( "( c / ( a - b ) )")
  print(' = '.join(map(treeToString, [expr, leftPushIn(expr), leftPullOut(leftPushIn(expr))])))

  expr = parseTree( "( ( a + b ) * c )")
  print(' = '.join(map(treeToString, [expr, rightPushIn(expr), rightPullOut(rightPushIn(expr))])))
  
  expr = parseTree( "( ( a - b ) / c )")
  print(' = '.join(map(treeToString, [expr, rightPushIn(expr), rightPullOut(rightPushIn(expr))])))
