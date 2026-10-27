# multiple plots in same graph | plt.legend()

'''
Write a Python program that:
1. Imports matplotlib.pyplot and numpy.
2. Creates an array of x-values from -5 to 5.
3. Calculates (y_1=x**2) and (y_2=x**3).
4. Plots both functions on the same graph.
5. Adds suitable labels to both lines, a title, and x- and y-axis labels.
6. Displays the graph.
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,6)
y1 = x**2
y2 = x**3

plt.plot(
    x, y1, 
    label="squares",
    color="red",
    marker=".",
    markersize=8,
    linestyle="-",
    linewidth=0.5
)

plt.plot(
    x, y2, 
    label="cubes",
    color="green",
    marker="+",
    markersize=8,
    linestyle="-",
    linewidth=0.5
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Plots on same Graph")
# plt.xlim(min(x)-5, max(x)+5)
# plt.ylim(min(y2)-5, max(y2)+5)

plt.legend()
plt.show()