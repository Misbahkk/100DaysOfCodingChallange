import pandas as pd
import numpy as np
#-----------------------------------------
'''Another way to create a data frame is by using a dictionary.
 Remember, a python dictionary is somehow similar to a Pandas series in that
 they have key-value pairs, just as Pandas series are label-value pairs (although
 this is a simplistic comparison for the sake of conceptualization)'''
# First, our dictionary
dico = {'X':[1,2,np.nan],'Y':[4,np.nan,np.nan],'Z':[7,8,9]}
print(dico)
#pasing the dicionary to dataframe
lable_df = 'A B C'.split()
df = pd.DataFrame(dico,lable_df)
'''It has the following default syntax:
 ``df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)``'''
print(df)
print('Remove NAN values:\n',df.dropna())
#Let us try a column-wise operation by specifying the axis=1.
print('Remove NAN values:\n',df.dropna(axis=1))
#drop rows with less than 2 actual values
print(df.dropna(thresh=2))
# Filter out columns in the data frame ‘df’ containing less than 2 actual data points
print(df.dropna(axis=1,thresh=2))

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
print('------------------------------------------------------------------------')
'''Next, let us use the 
.fillna( ) method to replace the missing values with our
 extrapolations.
 This method has the following syntax:
-> df.fillna(value=None, method=None, axis=None, inplace=False, limit=None,
 downcast=None, **kwargs)'''
print('replace our ‘NaN’ values with an ‘x’ marker\n',df.fillna('X'))
#Filling up missing data
print('\nReplacing missing value with mean in colum X\n')
print(df['X'].fillna(value=df['X'].mean()))
print('------------------------------------------------------------------------')
for i in 'X Y Z'.split():
   df[i].fillna(value=df[i].mean(),inplace=True)
print(df)


