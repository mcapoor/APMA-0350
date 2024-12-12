from sympy import *

s, t = symbols('s t',positive="True")
x = Function('x')
y = Function('y')

a_eq = exp(2*t) + 4*(t**3)
P7_a = laplace_transform(a_eq, t, s)[0]

b_eq = (2*(s-1)*exp(-3*s))/((s**2)-(2*s)+2)
P7_b = inverse_laplace_transform(b_eq, s, t)

c_eq = diff(y(t), t, 2) + 9*y(t) - Heaviside(t - 3) - 2*(t - 5) * Heaviside(t - 5)
P7_c = dsolve(c_eq, y(t), ics={y(0):0, diff(y(t), t).subs(t, 0):0})

print(f"Part A: {P7_a}")
print(f"Part B: {P7_b}")
print(f"Part C: {P7_c.rhs}")
plot(P7_c.rhs, (t, 0, 10))
