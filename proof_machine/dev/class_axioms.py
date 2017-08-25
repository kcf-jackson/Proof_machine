class Axioms:
	def __init__(self):
		self.axioms = []

	def hasAxiom(self, expr):
		for i in range(len(self.axioms)):
			if self.axioms[i] == expr:
				return True
		return False

	def addAxiom(self, expr):
		self.axioms.append(expr)

	def removeAxiom(self, expr):
		self.axioms.remove(expr)

	def showAxiom(self):
		print("--List of axioms--")
		for i in range(len(self.axioms)):
			print(self.axioms[i])
		print("--End of list--")

# Unit test
# print("Testing axiom class...")
# s = Axioms()
# s.addAxiom("f1<=f2")
# s.addAxiom("f2<=f3")
# s.showAxiom()
# print("Finish testing axiom class...")

def firstEqSecond(LHS, RHS, axiomList):
	return axiomList.hasAxiom(eq(LHS, RHS)) or axiomList.hasAxiom(eq(RHS, LHS))

def firstGSecond(LHS, RHS, axiomList):
	return axiomList.hasAxiom(g(LHS, RHS)) or axiomList.hasAxiom(l(RHS, LHS))

def firstLSecond(LHS, RHS, axiomList):
	LHS, RHS = RHS, LHS
	return firstGSecond(LHS, RHS, axiomList)

def firstGeqSecond(LHS, RHS, axiomList):
	return axiomList.hasAxiom(geq(LHS, RHS)) or axiomList.hasAxiom(leq(RHS, LHS)) or\
		firstGSecond(LHS, RHS, axiomList) or firstEqSecond(LHS, RHS, axiomList)
		
def firstLeqSecond(LHS, RHS, axiomList):
	LHS, RHS = RHS, LHS
	return firstGeqSecond(LHS, RHS, axiomList)

#def axiomToTuples(axiom)
