"""
    A. NBA dataset
    Using Pandas, read the CSV file from:
    https://media.geeksforgeeks.org/wp-content/uploads/nba.csv
    Print the size, shape, and dimension of the resulting DataFrame.
"""

import pandas as pd

url = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
df = pd.read_csv(url)

print(df.shape)
print(df.size)
print(df.ndim)
print(df.columns)
print(df.dtypes)

print(df.describe())
print(df.head())
