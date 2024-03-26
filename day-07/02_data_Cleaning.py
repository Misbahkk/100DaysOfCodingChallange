import pandas as pd

df = pd.read_csv("modern_arts.csv")

# print(df)

print(df['Gender'])

#remove Opening and closing breket
df['Gender']=df['Gender'].str.replace('(','').str.replace(')','')
print(df['Gender'])


#check the unique value 
print(df['Gender'].unique())

#we have this unique values (['Female' 'Male' '' 'male']) know we correct the male to upercase Male

df['Gender'] = df['Gender'].str.title()
print(df['Gender'].unique())

#Know remove the '' empty string to Unknown Gender
bol = df['Gender'] == ''
df.loc[bol,'Gender'] = 'Unknown Gender'
print(df['Gender'].unique())



#Know clean the Nationality column

#remove the () 
df['Nationality'] = df['Nationality'].str.replace('(','').str.replace(')','')
print(df['Nationality'])

df['Nationality'] = df['Nationality'].str.title()


bol2 = df['Nationality'] == ''
print(df.loc[bol2,'Nationality'])
df.loc[bol2,'Nationality'] = 'Nationality Unknown'
print(df['Nationality'].unique())
