# Base case: For any fixed a > 0, then a * 1_{x \geq a} \leq x, forall x in real.
# Invariant case: f(a) * 1_{x \geq a} \leq f(x)
# Also, if f is monotone, then x \geq a => f(x) \geq f(a) 
# if f is strictly monotone, f(x) \geq f(a) => x \geq a 

# if f1 leq f2, then E[f1] leq E[f2] (easy case)

# Jensen inequality
# if f is convex, then Ef(X) \leq f(EX)

execfile("class_axioms.py")
execfile("class_function.py")
execfile("expression.py")
execfile("util.py")

print("Testing axiom class...")
s = Axioms()
s.addAxiom("f1<=f2")
s.addAxiom("f2<=f3")
s.showAxiom()
print("Testing Indicator class")
f1 = Indicator(h = '1', a = 'a')
f2 = Indicator(h = '1', a = 'a2')
f1.view()
f2.view()
print("Created two Indicator objects")
s.addAxiom('1=1')
s.addAxiom('a>=a2')
s.showAxiom()
print(firstGeqSecond(f1.jumpAt, f2.jumpAt, s))

s.removeAxiom("a>=a2")
print(firstGeqSecond(f1.jumpAt, f2.jumpAt, s))

s.addAxiom('a2<=a')
print(firstGeqSecond(f1.jumpAt, f2.jumpAt, s))

print(f1.geq(f2, s))
print(f1.leq(f2, s))
print("Finish testing Indicator class")

f1 = Indicator(h = 'a', a = 'a')
s.addAxiom('a<=a')
x = Monomial()
x.view()
print(f1.leq(x, s))
s.addAxiom('a>1')
print(f1.leq(x, s))

s.showAxiom()
View([f1.view(), " <= ", x.view()])
View(takeExpectation([f1.view(), " <= ", x.view()]))

class linearFunction():
	def __init__(self, a = 0, b = 1):
		self.intercept = a
		self.slope = b
	def View(self):
		print(str(self.intercept) + " + " + str(self.slope) + " * X")



# b = indicatorFunction(h = 4, a = 0)

# print(leq(a, b))

# c = indicatorFunction(h = 2, a = "a")
# c.View()

# c = linearFunction()
# c.View()


