# Create a pandas column using for loop

import pandas as pd
import numpy as np

data = {'Voter_name': ['Geek1', 'Geek2', 'Geek3', 'Geek4',  
                           'Geek5', 'Geek6', 'Geek7', 'Geek8'],  
            'Voter_age': [15, 23, 25, 9, 67, 54, 42, np.NaN]} 


df = pd.DataFrame(data,columns=["Voter_name","Voter_age"])

eligible = []

for age in df["Voter_age"]:
    if age >= 18:
        eligible.append("Yes")
    elif age<18:
        eligible.append("No")
    else:
        eligible.append("Not Sure")


df["vote"] = eligible

print(df)
    