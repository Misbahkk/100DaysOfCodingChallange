import pandas as pd



# How to rename columns in Pandas DataFrame
# Method 1: Using rename() function

data = {'test': ['India', 'South Africa', 'England', 
                            'New Zealand', 'Australia'], 
            'odi': ['England', 'India', 'New Zealand', 
                            'South Africa', 'Pakistan'], 
            't20': ['Pakistan', 'India', 'Australia', 
                            'England', 'New Zealand']}


df = pd.DataFrame(data)

print(df.columns)
# df.rename(columns = {"test":"TEST"} ,inplace=True)

# print(df.columns)


# Example 2: Rename multiple columns. 

# df.rename(columns={"test":"TEST","odi":"ODI","t20":"T20"},inplace=True)
# print(df.columns)



# Method 2: By assigning a list of new column names 

# df.columns = ["TEST","ODI","T20"]
# print(df.columns)






# Method 3: Rename column names using DataFrame set_axis() function

# df.set_axis(['A','B','C'] , axis='columns' , inplace =True)
# print(df.columns)



# Method 4: Rename column names using DataFrame add_prefix() and add_suffix() functions

df = df.add_prefix('col_')
df = df.add_suffix('_1')
print(df.head())



# Method 5: Replace specific texts of column names using Dataframe.columns.str.replace function


df.columns = df.columns.str.replace('test','test_1')

df.columns = df.columns.str.replace('odi','ODI_1')
df.columns = df.columns.str.replace('t20',"T20_1")

print(df.columns)