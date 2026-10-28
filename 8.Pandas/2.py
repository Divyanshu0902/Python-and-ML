"""
    Day 8 assignment begins with a table containing Coordinate, Count, and Mismatch columns. 
    It asks you to create a dictionary, create a DataFrame, save it as a CSV file, and calculate standard scores.
"""

import pandas as pd

data = {
    "Coordinate": ["C1", "C2", "C3", "C4", "C5"],
    "Count": [300, 210, 230, 260, 270],
    "Mismatch": [5, 13, 14, 3, 2]
}

df = pd.DataFrame(data)
print("\nData Frame: \n",df)

df.to_csv("file2.csv",index=False)
loaded_data = pd.read_csv("file2.csv")
print("\nCSV File data: \n",loaded_data)


