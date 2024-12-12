import sympy as sp

t = sp.symbols('t')
x1 = sp.Function('x1')
x2 = sp.Function('x2')
deq1 = sp.diff(x1(t),t) - x1(t) + 4*x2(t)
deq2 = sp.diff(x2(t),t) - 4*x1(t) + 7*x2(t)
print(sp.dsolve([deq1,deq2],ics=({x1(0):3,x2(0):2})))


