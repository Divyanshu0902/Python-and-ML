'''
Write a Python program that:
1. Extracts the x-coordinates and y-coordinates into separate lists.
2. Plots them with the required styling.
3. Adds the title "2D Points Plot", x-label "X-axis" and y-label "Y-axis".
4. Sets both axis limits to their respective minimum minus 4 and maximum plus 4.
5. Saves the graph as r1.jpg and displays it.
'''

import matplotlib.pyplot as plt

points = [(1, 2), (3, 5), (4, 3), (6, 7), (8, 4)]

x = []
for i in range(len(points)):
    point = points[i]
    x.append(point[0])

y = []
for i in range(len(points)):
    point = points[i]
    y.append(point[1])

plt.plot(
    x,y,
    linestyle="--",
    color="green",
    marker=".",
    markersize=15,
    linewidth=2
)

plt.title("2D points plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.xlim(min(x)-4, max(x)+4)
plt.ylim(min(y)-4, max(y)+4)
# plt.xlim(0,10)
# plt.ylim(0,10)

plt.savefig("r1.jpg")

plt.show()