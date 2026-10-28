import pandas as pd

marks = pd.Series([10, 20, 30, 40, 50])

# Creating Data Frame using Python Dictionary : 
data = {
    "Name": ["Divyanshu", "Ronak", "Arka","Shashi"],
    "Marks": [88, 89, 86, 91],
    "Age": [23, 22, 20, 21]
}

df = pd.DataFrame(data)

print(df)