"""
    Question 1 — Create a dictionary, CSV file, and calculate Z-scores
    Question: Create a dictionary from the given table, save it as a CSV file, 
    and calculate the standard score for each Count value using (x-mean)/stddev.

    Coordinate	Count	Mismatch
    C1	300	5
    C2	210	13
    C3	230	14
    C4	260	3
    C5	270	2
"""


import pandas as pd

data = {
    "Coordinate": ["C1", "C2", "C3", "C4", "C5"],
    "Count": [300, 210, 230, 260, 270],
    "Mismatch": [5, 13, 14, 3, 2]
}

df = pd.DataFrame(data)
df.to_csv("coordinates.csv", index=False)

df["Z_Score"] = (
    df["Count"] - df["Count"].mean()
) / df["Count"].std()

print(df)
