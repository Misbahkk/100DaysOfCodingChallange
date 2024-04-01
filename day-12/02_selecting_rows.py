import pandas as pd 

'''Selecting rows in pandas DataFrame based on conditions
Let’s see how to Select rows based on some conditions in Pandas DataFrame.

Selecting rows based on particular column value using '>', '=', '=', '<=', '!=' operator.'''



data = {
    'Name':['Misbah','Maadeha','Laiba','Radia','Maham','Aina'],
    'Age':[21,22,23,21,20,23],
    'Course':['Python','Web','Python','Graphic','UI/UX','Web'],
    'Persantage':[89,60,78,57,91,88]
}

df = pd.DataFrame(data, columns=['Name','Age','Course','Persantage'])

print('Orignal Data\n',df)
print('#----------------------------------------------')
'''Code #1 : Selecting all the rows from the given dataframe in which 
‘Percentage’ is greater than 80 using basic method.'''
print('Percentage’ is greater than 80')
print(df[df['Persantage']>80])
print('#----------------------------------------------')

'''Code #3 : Selecting all the rows from the given dataframe in
 which ‘Percentage’ is not equal to 95 using Loc.'''
print('‘Percentage’ is not equal to 95')
print(df.loc[df['Persantage']!=91])
print('#----------------------------------------------')

'''Code #1 : Selecting all the rows from the given dataframe in which
 ‘Stream’ is present in the options list using basic method.'''

print('‘Stream’ is present in the options list')
options = ['Python','Graphic']
print(df[df['Course'].isin(options)])
print('#----------------------------------------------')


'''Code #3 : Selecting all the rows from the given dataframe in which
‘Stream’ is not present in the options list using .loc[].'''
print('‘Stream’ is not present in the options ')
print(df.loc[~df['Course'].isin(options)])

print('#----------------------------------------------')


'''Code #1 : Selecting all the rows from the given dataframe in which 
‘Age’ is equal to 21 and ‘Stream’ is present in the options list using basic method.
'''

print('Age’ is equal to 21 and ‘Stream’ is present in the options list ')
print(df[(df['Age'] == 21) & df['Course'].isin(options)])


print('#----------------------------------------------')
#---------------------------------------------------------------------
#Select any row from a Dataframe using iloc[] and iat[] in Pandas
'''In this article, we will learn how to get the rows from a dataframe as a list, 
using the functions ilic[] and iat[]. There are multiple ways to do get the rows as a 
list from given dataframe. Let’s see them will the help of examples. '''

data2 = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'], 
        'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
        'Cost':[10000, 5000, 15000, 2000]
        }
df2= pd.DataFrame(data2)

row_list = []

for i in range(df2.shape[0]):
    row_list.append(list(df2.iloc[i,:]))
print(row_list[:3])