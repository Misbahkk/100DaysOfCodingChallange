import pandas as pd 
# 
# 
#
"""
Using Pandas DataFrame to create Dataframe from List
Example #1:  We will use pd.DataFrame() function to create the dataframe from the list.
"""

data_1 = {"Misbah":[75,56,98,80],
        "Maadeha":[90,70,90,95],
        }
df_1 = pd.DataFrame(data_1)
print(df_1)


data_2 = {"SUbject":['Python','Java','DataScience','SQL'],"Misbah":[75,56,98,80],
        "Maadeha":[90,70,90,95],
        }
df_2 = pd.DataFrame(data_2)
print(df_2.transpose())


'''Using Pandas Dataframe with the index parameter

'''
print()
print("Example #1: Providing index list to dataframe ")
data_3 = {"SUbject":['Python','Java','DataScience','SQL'],"Misbah":[75,56,98,80],
        "Maadeha":[90,70,90,95],
        }
df_3 = pd.DataFrame(data_3,index=["sub_1","sub_2","sub_3","sub_4"])
print(df_3)

