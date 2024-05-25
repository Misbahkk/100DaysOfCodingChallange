import pandas as pd 
import numpy as np 

# Import the CSV file into Jupyter notebook, assign it to a variable
# ‘Sal’, and display the first 5 values.
df = pd.read_csv('Salaries.csv')
print(df)

head_5=df.head()
print('Starting 5 rows:\n',head_5)
tail1=df.tail()
print('ENding 5 rows : \n',tail1)
 #What is the highest pay (including benefits)?    
#567595.4
maximum =df.max()
print('Maximum Benifit Pay: ',maximum)
'''According to the data, what is ‘MONICA FIELDS’s Job title, and
 how much does she make plus benefits? Answer:  Deputy Chief
 of the Fire Department, and $ 261,366.14 .'''
jobtitle=df.loc[df['EmployeeName']=='MONICA FIELDS','JobTitle'].values[0]
paybenifite = df.loc[df['EmployeeName'] == 'MONICA FIELDS', 'TotalPayBenefits' ]
print(df['EmployeeName'],jobtitle,paybenifite)
'''Finally, who earns the highest basic salary (minus benefits), and
 by how much is their salary higher than the average basic salary.
 Answer: NATHANIEL FORD earns the highest. His salary is
 higher than the average by $ 492827.1080282971'''
#ya mujh sa hova nh
df['EmployeeName'] == 'MONICA FIELDS'
