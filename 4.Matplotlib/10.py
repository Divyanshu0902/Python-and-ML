## Bar Graph: 

'''
Using the following data, write a program to display a bar chart of monthly face cream sales.
months = ["Jan", "Feb", "Mar", "Apr", "May"]sales = [250, 300, 350, 400, 450]

Requirements:
1. Use plt.bar().
2. Add an appropriate title.
3. Label both axes.
4. Display the chart using plt.show().
'''

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [250, 300, 350, 400, 450]

# plt.bar(months, sales)
plt.bar(months, sales, color="green", width=0.6)
plt.title("Bar Graph")
plt.xlabel("Months")
plt.ylabel("Units Sold")

plt.xticks(range(5),months)
plt.yticks(range(0,501,50))

plt.show()