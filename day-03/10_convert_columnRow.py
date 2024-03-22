import pandas as pd

#Convert a column to row name/index in Pandas

"""Pandas provide a convenient way to handle data and its transformation. 
Let’s see how can we convert a column to row name/index in Pandas. """


#Create a dataframe first with dict of lists. 


data = {'Name':["Akash", "Geeku", "Pankaj", "Sumitra","Ramlal"],
       'Branch':["B.Tech", "MBA", "BCA", "B.Tech", "BCA"],
       'Score':["80","90","60", "30", "50"],
       'Result': ["Pass","Pass","Pass","Fail","Fail"]}


df = pd.DataFrame(data)
print(df)

#Method #1: Using set_index() method. 
df_1 = df.set_index('Name')
print(df_1)

df_1.index.names = [None]
print(df_1)

#Method #2: Using pivot() method.

df_2=df.pivot(index='Result',columns='Name',values='Score')
# Remove the column name 'Name'
df_2.columns.name = None

df_2.index.names = [None]
print(df_2)