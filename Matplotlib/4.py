# multiple axes pairs in same page | plt.subplot()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 6)

plt.subplot(2, 2, 1)
plt.plot(x, x)
plt.title("x")

plt.subplot(2, 2, 2)
plt.plot(x, x**2)
plt.title("x squared")

plt.subplot(2, 2, 3)
plt.plot(x, x**3)
plt.title("x cubed")

plt.subplot(2, 2, 4)
plt.plot(x, x**4)
plt.title("x to the power 4")

plt.tight_layout()
plt.show()