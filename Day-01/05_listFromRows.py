#Create a list from rows in Pandas dataframe

import pandas as pd

"""Python list is easy to work with and also list has a lot of 
in-built functions to do a whole lot of operations on lists. """

#Solution #1: In order to iterate over the rows of the Pandas dataframe we can use 
#DataFrame.iterrows() function and then we can append the data of each row to the end of the list.

data = {'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'], 
        'Event':['Music', 'Poetry', 'Theatre', 'Comedy'], 
        'Cost':[10000, 5000, 15000, 2000]}

df = pd.DataFrame(data)

print(df)



list_row=[]


for indeex,row in df.iterrows():
    my_list=[row.Date,row.Event,row.Cost]

    list_row.append(my_list)

print(list_row)