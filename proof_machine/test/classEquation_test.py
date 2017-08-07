import os
os.chdir('../')
exec(open('load.py').read())

l = parseTree('a')
r = parseTree('b')
r2 = parseTree('c')

a = Equation(l, '<=', r)
b = Equation(r2, '>', r)
a.view()
b.view()
transitive(a, b).view()

a = Equation(r, '>=', l)
b = Equation(r2, '>', r)
a.view()
b.view()
transitive(a, b).view()
