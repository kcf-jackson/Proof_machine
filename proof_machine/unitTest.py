import os 
os.chdir('../')
exec(open('load.py').read())

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
