import numpy as np
import matplotlib as plt
#Calculates forward Euler Method Aproximation
a = 0 #The starting value in the range
b = 10 #The ending value in the range
y0 = 1 #The initial condition
n = 101 #The number of steps plus 1

h = (b - a) / (n - 1)
t = np.linspace(a, b, n)
y = np.zeros([n])

y[0] = y0 #if the initial condition does not correspond to 0, change this value and fudge the iteration below

for i in range(1, n): 
    y[i] = y[i - 1] + h * (-y[i - 1] + np.sin(t[n - 1]))
    #Change this line to correspond to the ODE

for i in range(n):
    print(t[i], y[i])

plt.plot(t,y,'o')
plt.xlabel("Value of t")
plt.ylabel("Value of y")
plt.title("Approximate Solution with Forward Euler's Method")
plt.show()