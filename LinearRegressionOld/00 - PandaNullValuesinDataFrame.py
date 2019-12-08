# https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
import pandas as pd

# Count the Null Columns

train = pd.read_csv("train.csv")
null_columns = train.columns[train.isnull().any()]

print(train[null_columns].isnull().sum())

# So there are lots of different columns containing null values.
# What if we want to find the solitary row which has "Electrical" as null?


print(train[train["Electrical"].isnull()][null_columns])

# And what if we want to return every row that contains at least one null value?
# That’s not too difficult – it’s just a combination of the code in the previous two sections.
# All Null Columns
print(train[train.isnull().any(axis=1)][null_columns].head())