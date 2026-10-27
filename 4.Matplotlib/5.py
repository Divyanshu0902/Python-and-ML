'''
Plot the functions \(f(x)=x,\ x^2,\ x^3,\ x^4,\ x^5,\ x^6\) 
in separate graphs but in the same figure, with a title and labels.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)
y1 = x
y2 = x**2
y3 = x**3
y4 = x**4
y5 = x**5
y6 = x**6

plt.subplot(2,3,1)
plt.plot(x,y1)
plt.title("X raised to power 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(2,3,2)
plt.plot(x,y2)
plt.title("X raised to power 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(2,3,3)
plt.plot(x,y3)
plt.title("X raised to power 3")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(2,3,4)
plt.plot(x,y4)
plt.title("X raised to power 4")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(2,3,5)
plt.plot(x,y5)
plt.title("X raised to power 5")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.subplot(2,3,6)
plt.plot(x,y6)
plt.title("X raised to power 6")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.tight_layout()
plt.show()
