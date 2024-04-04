import pandas as pd


data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Alice', 'Bob', 'Emily', 'Mike'],
    'Age': [25, 30, None, 35, 40],
    'Gender': ['Male', 'Female', 'male', 'Female', 'Male'],
    'Income': [50000, 60000, 70000, 55000, None],
    'Education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters']
}

df = pd.DataFrame(data)
print(df)

# Strategies for handling missing values include filling them with a specific value
# like mean
mean_nan = df['Age'].mean()
df['Age']=df['Age'].fillna(mean_nan)
print(df['Age'])

mean_income = df['Income'].mean()
df['Income']= df['Income'].fillna(mean_income)
print(df['Income'])
# Duplicate Rows: NO dublicated rows
print(df.drop_duplicates())

print(df.info())


# correct the gender 
df['Gender']= df['Gender'].str.title()
print(df['Gender'])

# Convert the data type of age and income into int

df['Age'] =df['Age'].astype(int)
df['Income'] = df['Income'].astype(int)
print(df.info())

new_df = df.pivot_table(index='Age',values='Name')
print(new_df)