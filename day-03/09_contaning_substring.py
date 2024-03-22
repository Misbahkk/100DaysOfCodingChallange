#Get all rows in a Pandas DataFrame containing given substring
'''Let’s see how to get all rows in a Pandas DataFrame containing given substring with the help of different examples.'''

import pandas as pd 

data = {'Name': ['Geeks', 'Peter', 'James', 'Jack', 'Lisa'], 
        'Team': ['Boston', 'Boston', 'Boston', 'Chele', 'Barse'], 
        'Position': ['PG', 'PG', 'UG', 'PG', 'UG'], 
        'Number': [3, 4, 7, 11, 5], 
        'Age': [33, 25, 34, 35, 28], 
        'Height': ['6-2', '6-4', '5-9', '6-1', '5-8'], 
        'Weight': [89, 79, 113, 78, 84], 
        'College': ['MIT', 'MIT', 'MIT', 'Stanford', 'Stanford'], 
        'Salary': [99999, 99994, 89999, 78889, 87779]}

df = pd.DataFrame(data,index=['ind1', 'ind2', 'ind3', 'ind4', 'ind5'])

print(df,'\n')

#Code #1: Check the values PG in column Position
df_pg = df[df['Position'].str.contains('PG')]
print(df_pg)

#Code #3: Filter all rows where either Team contains ‘Boston’ or College contains ‘MIT’.
df_2 = df[df['Team'].str.contains('Boston') | df['College'].str.contains('MIT')]
print(df_2)

#Code #4: Filter rows checking Team name contains ‘Boston and Position must be PG.
df_3 = df[df['Team'].str.contains('Boston') & df['Position'].str.contains('PG')]
print(df_3)


#Code #5: Filter rows checking Position contains PG and College must contains like UC.
df_4 = df[df['Position'].str.contains('PG') & df['College'].str.contains('MIT')]
print(df_4)