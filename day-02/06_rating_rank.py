###########Ranking Rows of Pandas DataFrame

"""To rank the rows of Pandas DataFrame we can use the DataFrame.rank() 
method which returns a rank of every respective index of a series passed. 
The rank is returned on the basis of position after sorting."""

import pandas as pd
#
'''Example #1 :

Here we will create a DataFrame of movies and rank them based on their ratings.'''


movies =  {'Name': ['The Godfather', 'Bird Box', 'Fight Club'], 
         'Year': ['1972', '2018', '1999'], 
         'Rating': ['9.2', '6.8', '8.8']}

df = pd.DataFrame(movies)

print(df)
#Add new column rating rate
df['Rating_rate'] = df['Rating'].rank(ascending=1)

df = df.set_index('Rating_rate')

print(df)

df.sort_index()

print(df)

print('------------------------------------------------------')
"""Example #2
Let’s take an example of marks scored by 4 students. 
We will rank the students based on the highest mark they have scored."""


student_details = {'Name':['Raj', 'Raj', 'Raj', 'Aravind', 'Aravind', 'Aravind', 
                            'John', 'John', 'John', 'Arjun', 'Arjun', 'Arjun'], 
                   'Subject':['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics', 
                            'Chemistry', 'Maths', 'Physics', 'Chemistry', 'Maths', 
                            'Physics', 'Chemistry'], 
                   'Marks':[80, 90, 75, 60, 40, 60, 80, 55, 100, 90, 75, 70] 
               } 

df2 = pd.DataFrame(student_details)

print(df2)

df2['Marks_rank'] = df2['Marks'].rank(ascending=1)

df2=df2.set_index('Marks_rank')
df2=df2.sort_index()
print(df2)
