import pandas as pd 

"""How to iterate over rows in Pandas Dataframe"""
"""Python is a great language for doing data analysis, primarily because of the fantastic ecosystem of data-centric Python packages."""
'''Pandas is one of those packages and makes importing and analyzing data much easier.'''
#---------------------------------------------
#Let’s see the how to iterate over rows in Pandas Dataframe using iterrows() and itertuples() :
#Method #1: Using the DataFrame.iterrows() method
#This method iterated over the rows as (index, series) pairs.

# data = [
#     {'Name':'Misbah','age':22},
#     {'Name':'Maadeha','age':20},
#     {'Name':'Laiba','age':21},
# ]

# df = pd.DataFrame(data)
# print("Orignal data\n",df)

# print("After apply iterrows()\n")

# for index , row in df.iterrows():
#     print(row['Name'],row['age'])
# print('#--------------------------------------------------------------')

#------------------------------------------------------
'''Method #2: Using the DataFrame.itertuples() method
This method returns a named tuple for every row. 
getattr() function can be used to get the row attribute in the returned tuple. 
This method is faster than Method #1. '''

# print("After apply itertuple()\n")
# for row in df.itertuples():
#     print(getattr(row,'Name'),getattr(row,'age'))

# print('#--------------------------------------------------------------')

#--------------------------------------------------------------
#--------------------------------------------------------------
    
'''Different ways to iterate over rows in Pandas Dataframe'''
#--------------------------------------------------------------
#Method 1: Using the index attribute of the Dataframe.

info = {
    'Name':['Misbah','Maadeha','Laiba','Radia'],
    'Age':[21,22,23,28],
    'Course':['Python','Web','Cyber Security','Graphic'],
    'Persantage':[89,90,78,87]
}
df_info = pd.DataFrame(info,columns=['Name','Age','Course','Persantage'])

print('Oraginal Data\n',df_info)

print('#--------------------------------------------------------------')
print('After Applying Itrative method\n')

for indx in df_info.index:
    print(df_info['Name'][indx],df_info['Course'][indx])



print('#--------------------------------------------------------------')
'''Method 2: Using loc[] function of the Dataframe. '''
print('After Applying loc[] function method\n')
for i in range(len(df_info)):
    print(df_info.loc[i,'Name'],df_info.loc[i,'Age'])



print('#--------------------------------------------------------------')
'''Method 3: Using iloc[] function of the DataFrame. '''
print('After Applying iloc[] function method\n')
for i in range(len(df_info)):
    print(df_info.iloc[i,0],df_info.iloc[i,2])


