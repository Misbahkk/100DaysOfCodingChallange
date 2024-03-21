import pandas as pd

#Select row with maximum and minimum value in Pandas dataframe


data1 = {'Driver': ['Hamilton', 'Vettel', 'Raikkonen',
                    'Verstappen', 'Bottas', 'Ricciardo',
                    'Hulkenberg', 'Perez', 'Magnussen',
                    'Sainz', 'Alonso', 'Ocon', 'Leclerc',
                    'Grosjean', 'Gasly', 'Vandoorne',
                    'Ericsson', 'Stroll', 'Hartley', 'Sirotkin'],
 
        'Points': [408, 320, 251, 249, 247, 170, 69, 62, 56,
                    53, 50, 49, 39, 37, 29, 12, 9, 6, 4, 1],
 
        'Age': [33, 31, 39, 21, 29, 29, 31, 28, 26, 24, 37,
                 22, 21, 32, 22, 26, 28, 20, 29, 23]}

df =pd.DataFrame(data1)

# print(df)

print("Example 1: Shows max on Driver, Points, and Age columns. ")
print(df.max())

print("Example 2: Who scored max points ")

print(df[df.Points == df.Points.max()])

print(" Example 3: What is the maximum age ")
print(df.Age.max())


print("Example 4: Which row has maximum age in the Dataframe | who is the oldest driver? ")
print(df[df.Age == df.Age.max()])

print("Example 1: Shows min on Driver, Points, Age columns. ")

print(df.min())

print("Example 2: Who scored fewer points ")

print(df[df.Points == df.Points.min()])

print("Example 3: Which row has minimum age in the Dataframe who is the youngest driver ")
print(df[df.Age == df.Age.min()])