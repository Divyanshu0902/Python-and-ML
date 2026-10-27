'''
plot:
f(x)=2x+4, g(x)=4x^2+5x+4 in the same axis with a legend.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)
fx = 2*x + 4
gx = 4*x**2 + 5*x + 4

plt.plot(
    x,fx,
    label = "f(x)=2x+4"
)

plt.plot(
    x,gx,
    label = "g(x)=4x^2+5x+4"
)

plt.title("Polinomial Graphs")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig("Polynomial.jpg")
plt.legend()
plt.show()