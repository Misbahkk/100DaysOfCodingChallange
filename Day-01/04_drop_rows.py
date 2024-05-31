import pandas as pd 

#Drop rows from the data frame based on certain conditions applied on a column
                             
df = pd.read_csv('nba.csv')

# print(df.head())

## Filter rows where the player's age is 25 or older
age_row = df[df['Age']>=25]
# print(age_row.head(15))

'''Example 1: As we can see in the output, the returned Dataframe only contains 
those players whose age is not between 20 to 25 age using df.drop(). '''

imdexAge = df[(df['Age']>=20)  & (df['Age']<=25)].index
df.drop(imdexAge,inplace=True)
print(df.head())


'''Example 2: Here, we drop all the rows whose names and Positions are associated with
 ‘John Holland‘ or ‘SG’ using df.drop().'''

filter_name = df[(df['Name'] == 'John Holland') | (df['Position'] == 'SG')].index
df.drop(filter_name,inplace=True)
print(df.head())



# Delete Rows Based on Multiple Conditions on a Column Using query()
"""In this example, we are using query() function to delete rows based on multiple conditions on a column. 
Below code creates a DataFrame and filters it to keep only individuals aged 30 or younger using the 
`query` function. The resulting DataFrame is printed."""

df_query = df.query('Age <= 30')
print(df_query.head(15))

""". Below code generates a DataFrame and filters it to retain rows 
where the ‘age’ is 30 or less, displaying the modified DataFrame."""

df_loc = df.loc[df['Age']<=30]
print(df_loc.head())



df_weight = df['Weight']<=200

df_condition = df[~df_weight]
print(df_condition)
