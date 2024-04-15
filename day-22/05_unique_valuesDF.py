# Get unique values from a column in Pandas DataFram

import pandas as pd

# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B4'],
    'C': ['C1', 'C2', 'C3', 'C3', 'C3'],
    'D': ['D1', 'D2', 'D2', 'D2', 'D2'],
    'E': ['E1', 'E1', 'E1', 'E1', 'E1']}

df = pd.DataFrame(data)

print(df)


# Get the Unique Values of ‘B’ Column

print(df.B.unique())

# Get the Unique Values of Pandas in ‘E’ Column
print(df.E.unique())

# Get Number of Unique Values in a Column
print(df.C.nunique(dropna=True))


# Eliminate Duplicate Values from a Column using set()
unique_value_set = set(df['C'])
print(unique_value_set)


# Using pandas.concat() and Unique() Methods

# unique_concat_value = pd.concat([df[col].unique() for col in df.columns])
# print(unique_concat_value)


# Using Series.drop_duplicates()

df['A'] = df['A'].drop_duplicates()
df['C'] = df['C'].drop_duplicates()

print(df)