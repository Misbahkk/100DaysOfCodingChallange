import pandas as pd



df = pd.read_csv("modern_arts.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.shape[0])
print(df.shape[1])
print(type(df))
print(df['Gender'])

multi_columns =['Artist','EndDate']
print(df[multi_columns])

print(df.iloc[0])
print(df.iloc[[1,5],[1,3]])
df=df.set_index('Nationality')
print(df.head())
print(df.columns)
df_loc = df.loc[["(American)","(Spanish)"],["Artist","Date"]]
print(df_loc)