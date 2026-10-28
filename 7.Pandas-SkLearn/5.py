"""
Question 5 — NBA CSV and Iris dataset
Question: Use Pandas to read the NBA CSV from the assignment URL and print the size, shape, and dimension. Load the Iris dataset, preview the data, display its features and class levels, replace class values 0, 1, and 2 with Setosa, Versicolor, and Virginica, group by species, calculate the mean sepal length and width per group,
and display the maximum and standard deviation of each feature.
"""


import pandas as pd
from sklearn.datasets import load_iris

# NBA dataset
url = "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv"
nba = pd.read_csv(url)

print("Size:", nba.size)
print("Shape:", nba.shape)
print("Dimensions:", nba.ndim)

# Iris dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["Species"] = iris.target
df["Species"] = df["Species"].map({
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
})

print(df.head())
print("Features:", iris.feature_names)
print("Class levels:", df["Species"].unique())

grouped = df.groupby("Species")

print("Mean sepal length and width:")
print(
    grouped[
        ["sepal length (cm)", "sepal width (cm)"]
    ].mean()
)

print("Maximum of each feature:")
print(df[iris.feature_names].max())

print("Standard deviation of each feature:")
print(df[iris.feature_names].std())
