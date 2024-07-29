#Sorting rows in pandas DataFrame
import pandas as pd

"""Pandas DataFrame is a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns)."""
'''We often need to do certain operations on both rows and columns while handling the data.'''
#Let’s see how to sort rows in Pandas DataFrame.
# 
data =  {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],  
        'Maths': [8, 5, 6, 9, 7],  
        'Science': [7, 9, None, 4, 7], 
        'English': [7, 4, 7, 6, 8]} 

df = pd.DataFrame(data)
print(df)
#Code #1: Sorting rows by Science


df = df.sort_values(by='Science',ascending=0)
print(df)
                       
#Code #2: Sort rows by Maths and then by English.                         

df = df.sort_values(by=['Maths','English'])

print(df)

#Code #3: If you want missing values first.
df = df.sort_values(by='Science',na_position='first')
print(df)
