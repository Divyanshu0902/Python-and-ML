# pie chart | plt.pie()

'''
Plot a pie chart showing the percentage of grades obtained in DBMS. The data is given below:

| Grade | Percentage |
|---|---:|
| O | 23 |
| E | 34 |
| A | 12 |
| B | 5 |

Use plt.pie() to plot the data, with L as the list of labels and autopct='%.2f' to display the percentages.
'''

import matplotlib.pyplot as plt

data = [23, 34, 12, 5]
L = ['O', 'E', 'A', 'B']

plt.pie(data, labels=L, autopct="%.2f")

plt.title("Plotting Pie Chart")
plt.show()