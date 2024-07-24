#Pandas DataFrame with Two-dimensional List
"""
Using pd.DataFrame()
Using pd.DataFrame.from_records()
Using pd.DataFrame.from_dict()
Using Specifying Data Types
"""
##

#---------------------------------------------------------
import pandas as pd
import numpy as np


#Create Pandas Dataframe from 2D List using pd.DataFrame()

# lst_1 = [[1,1],[2,4],[3,9],[4,16],[5,25]]

# df_1 = pd.DataFrame(lst_1,columns =['Num',"Squree"])
# print(df_1)

#Create Pandas Dataframe from 2D List using pd.DataFrame.from_records()

# lst_2 = [["misbah",21,"CS"],["Maadeha",21,"CS"],["Radia",20,"CS"],["Hafsa",22,"BBA"],["JiyA",19,"Pysic"]]
# columns =["Name","Age","Department"]
# df_2 = pd.DataFrame.from_records(lst_2,columns =columns)
# print(df_2)


#Create Pandas Dataframe from 2D List using pd.DataFrame.from_dict()


# lst_3 = [["misbah",21,"CS"],["Maadeha",21,"CS"],["Radia",20,"CS"],["Hafsa",22,"BBA"],["JiyA",19,"Pysic"]]
# columns =["Name","Age","Department"]
# df_3 = pd.DataFrame.from_dict(dict(zip(columns,zip(*lst_3))))
# print(df_3)




"""
Create Pandas Dataframe using list of lists
There are various methods to create a Pandas data frame using a list of lists. Here, we are discussing some generally used methods that are following

Using pd.DataFrame() Function
Handling Missing Values
DataFrame with Different Data Types
"""

# print("\nCreate Pandas Dataframe using list of lists\n")
# print("Using pd.DataFrame() function\n")

# lst_4 = [["Misbah",56],["Maadeha",52],["Radia",90],["Maham",53],["Laiba",50]]

# columns = ["Name","Roll No."]

# df_4 = pd.DataFrame(lst_4,columns=columns)
# print(df_4)



# print("\nHandling Missing Values\n")

# lst_5 = [["misbah",None,"CS"],["Maadeha",21,None],["Radia",20,"CS"],["Hafsa",None,"BBA"],["JiyA",19,None]]
# columns =["Name","Age","Department"]
# df_5 = pd.DataFrame(lst_5,columns=columns)
# df_5 = df_5.replace({None:np.NaN})
# print(df_5)

"""
DataFrame With Different Data Types
Below code creates a Pandas DataFrame from a list of lists, 
converting the ‘Age’ column to numeric format and handling errors, with the result printed. 
The ‘Age’ values, initially a mix of numbers and strings, are corrected to numeric format.
"""
# print("\nDataFrame With Different Data Types\n")

# lst_6 = [["Misbah",56,"Matli"],
#          ["Maadeha",52,"Kotri"],
#          ["Radia","90","Mirpurekhas"],
#          ["Maham",53,"Sangertr"],
#          ["Laiba",50,"Mirpurekhas"]]

# columns = ["Name","Roll No.","City"]

# df_6 = pd.DataFrame(lst_6,columns=columns)
# df_6["Roll No."] = pd.to_numeric(df_6["Roll No."],errors="coerce")
# print(df_6)



"""In this example the below code uses pandas to create a DataFrame from a list of lists,
 assigns column names (‘Col_1’, ‘Col_2’, ‘Col_3’), prints the original DataFrame,
   transposes it, and prints the result.
 Transposing swaps rows and columns in the DataFrame."""

# print("\nTransposing swaps rows and columns in the DataFrame.\n")

# lst_7 = [[2,4,8],[3,9,14],[4,8,12]]

# columns=["col_1","col_2","col_3"]

# df_7 = pd.DataFrame(lst_7,columns=columns)

# print(df_7,"\n")

# print("Transpose the Above DataFrame")

# df_7 =df_7.transpose()

# print(df_7)


"""Creating a Pandas dataframe using list of tuples
Pandas is famous for data manipulation in Python. We can create a DataFrame from a list of simple tuples,
and can even choose the specific elements of the tuples we want to use."""


# print("\nExample 1: In this example, we will simply pass the tuple to the DataFrame constructor which will return a pandas dataframe.\n")

# lst_tuple = [
#     ("Misbah","kaimKhani",21),
#     ("Maadeha","Shaik",20),
#     ("Laiba","Shaik",21)
# ]

# df_8 = pd.DataFrame(lst_tuple,columns=["Name","Surname","Age"])

# print(df_8)


# print("\nExample 2: In this example, we will use the df.from_records() to create the dataframe from the list of tuples.\n")

# lst_tuple_2 = [
#     ("Misbah","kaimKhani",21),
#     ("Maadeha","Shaik",20),
#     ("Laiba","Shaik",21)
# ]

# df_9 = pd.DataFrame.from_records(lst_tuple_2,columns=["Name","Surname","Age"])

# print(df_9)



"""Using df.pivot() function
Here we will create a Pandas Dataframe using a list of tuples using the df.pivot() function method.

Example 3: Creating pivot table by using three columns"""

print("\nExample 3: Creating pivot table by using three columns\n")

lst_tuple_3 = [
    ("Misbah",56,"CS"),
    ("Jiya",53,"Physic"),
    ("Maadeha",52,"CS"),
    ("Hafsa",50,"BBA"),
    ("Alisha",40,"Physic"),
    ("Sidra",56,"ARTS"),
]
# lst_tuple_3 = [
#     ("Misbah",56,2),
#     ("Jiya",53,3),
#     ("Maadeha",52,2),
#     ("Hafsa",50,4),
#     ("Alisha",40,5),
#     ("Sidra",56,3),
# ]

df_10 = pd.DataFrame(lst_tuple_3,columns=["name","RollNumber","Department"])
#The pivot() method in pandas DataFrames expects specific arguments to determine how to transform the data.
x = df_10.pivot(index="name",columns="Department",values="RollNumber")
print(x)
