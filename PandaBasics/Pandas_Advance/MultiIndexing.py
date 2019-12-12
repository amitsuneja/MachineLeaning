import pandas as pd
df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=[["A", "AA"], ["B", "BB"]])
print(df)
print("_____________")
print(df["AA"])
print("_____________")
print(df["A","B"])
print("_____________")
print(df["A"])
#  A["B"] , A["BB"] - incorrect selection
