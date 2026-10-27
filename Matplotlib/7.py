# Histogram | plt.hist()

'''
data = [4, 5, 5, 7, 6, 8, 8, 9, 4, 4,
        4, 4, 5, 5, 7, 7, 8, 8, 8]
Write a program that:
1. Plots the histogram.
2. Sets the title to "Plotting Histogram".
3. Sets the y-axis label to "Frequency".
4. Sets the x-axis limits from min(data) - 4 to max(data) + 4.
5. Saves the graph as a file
'''

import matplotlib.pyplot as plt

data = [4, 5, 5, 7, 6, 8, 8, 9, 4, 4,
        4, 4, 5, 5, 7, 7, 8, 8, 8]

plt.hist(data)
plt.title("Plotting Histogram")
plt.xlabel("Intervals")
plt.ylabel("Frequency")
plt.xlim(min(data)-4, max(data)+4)

plt.savefig("histogram.jpg")
plt.show()