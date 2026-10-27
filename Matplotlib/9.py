'''
Consider a company which needs to display the number of units sold per month for each product 
using multiline plots (i.e., a separate plot line for each product).

The products are:
- faceCreamSalesData
- faceWashSalesData
- toothPasteSalesData
- bathingsoapSalesData
- shampooSalesData
- moisturizerSalesData

Requirements:
1. Display the monthly sales of all six products using a separate line for each product.
2. Provide an appropriate legend and place it in the upper-left corner using the loc property.
3. Use plt.xticks() to provide labels for the months on the x-axis.
4. Use plt.yticks() to set the values displayed on the y-axis.
Note: The assignment names the six sales-data variables but does not provide their numerical values in this question
'''

import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

faceCreamSalesData = [250, 270, 300, 320, 350, 370, 400, 420, 390, 360, 340, 380]
faceWashSalesData = [200, 220, 240, 260, 280, 300, 320, 310, 290, 270, 260, 280]
toothPasteSalesData = [520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630]
bathingsoapSalesData = [700, 720, 750, 780, 800, 830, 850, 870, 900, 920, 950, 980]
shampooSalesData = [300, 310, 330, 350, 370, 390, 410, 430, 420, 400, 380, 410]
moisturizerSalesData = [180, 190, 210, 230, 250, 270, 290, 300, 280, 260, 240, 270]

plt.plot(months, faceCreamSalesData,label="Face Cream")
plt.plot(months, faceWashSalesData,label="Face Wash")
plt.plot(months, toothPasteSalesData,label="Tooth Paste")
plt.plot(months, bathingsoapSalesData,label="Bathing Soap")
plt.plot(months, shampooSalesData,label="Shampoo")
plt.plot(months, moisturizerSalesData,label="Moisturizer")

plt.xticks(range(12), months)
plt.yticks(range(0,1001, 100))
plt.legend(loc = "upper left")

plt.xlabel("Months")
plt.ylabel("Units Sold")
plt.title("Sales Graph")

plt.savefig("SalesGraph.jpg")
plt.show()