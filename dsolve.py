from sympy import *

t = symbols('t')
y = Function('y')
deq = (t * diff(y(t), t)) + ((t + 1) * y(t)) - (2 * t * exp(-t)) 
ysoln = dsolve(deq, y(t), ics={y(1): 2})

print(ysoln)
plot(ysoln.rhs,(t, -5, 5), ylim=[-20, 2])