import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

# print(iris.data)
# print(iris.feature_names)
# print(iris.target_names)
# print(iris.target)

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["Species"] = iris.target

df["Species"] = iris.target_names[iris.target]

# print(df.head())

# grouped = df.groupby("Species")
# selected = grouped[["sepal length (cm)", "sepal width (cm)"]]
# result = selected.mean()

# print(result)

# maximum and std of each feature column---
features = df[iris.feature_names]

print("\nMaximum of each feature: \n", features.max())
print("\nStandard Deviation of each feature: \n", features.std())