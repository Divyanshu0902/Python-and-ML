import matplotlib.pyplot as plt

data = [20, 60, 80]
lbl = ["2019", "2020", "2021"] 

plt.pie(data, labels=lbl, autopct="%.2f")

plt.show()