# How to get column names in Pandas dataframe

import pandas as pd


df = pd.read_csv("nb.csv")

print(df)


# Simply iterating over columns 

for col in df.columns:
    print(col)


# Method #2: Using columns attribute with dataframe object 

print(list(df.columns))


# Method #3: Using keys() function: It will also give the columns of the dataframe.

print(df.keys())


# Method #4:  column.values method returns an array of index. 

print(df.index)


#  Method #5: Using tolist() method with values with given the list of columns.  Method #5: Using tolist() method with values with given the list of columns. 

print(df.columns.values.tolist())


# Method #6: Using sorted() method : sorted() method will return the list of columns sorted in alphabetical order. 

print(sorted(df))