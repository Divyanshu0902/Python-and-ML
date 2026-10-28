# Pandas — Lesson 2: Selecting, Filtering and Statistics

import pandas as pd

data = {
    "Coordinate": ["C1", "C2", "C3", "C4", "C5"],
    "Count": [300, 210, 230, 260, 270],
    "Mismatch": [5, 13, 14, 3, 2]
}

df = pd.DataFrame(data)

# Selecting Column --
# Count = df[["Count", "Mismatch"]]
# print(Count)

# Filtering Rows ---
# x = df[df["Count"]>250]
# print(x)

# AND: both conditions must be true
# print(df[(df["Count"] > 250) & (df["Mismatch"] < 5)])

# OR: at least one condition must be true
# print(df[(df["Count"] > 250) | (df["Mismatch"] > 10)])

# Calculating Statistics:--
# print(df["Count"].mean())    # Average
# print(df["Count"].median())  # Median
# print(df["Count"].max())     # Maximum
# print(df["Count"].min())     # Minimum
# print(df["Count"].std())     # Standard deviation
# print(df["Count"].sum())     # Sum

#calculate the standard score for each Count value using the expression \((x-\text{mean})/\text{stddev}\)

# i.e. add column (x - mean)/stddev for each count value

mean = df["Count"].mean()
stddev = df["Count"].std()

df["Standard-Score"] = (df["Count"] - mean) / stddev

print(df)

