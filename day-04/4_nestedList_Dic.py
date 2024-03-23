#Python | Convert list of nested dictionary into Pandas dataframe
"""Convert Nested List of Dictionary into Pandas Dataframe
Below are the methods that will be used

Using from_dict(orient=’index’)
Native Method
"""

import pandas as pd

# countries = {
#     "1": {"Country": "New Country 1",
#           "Capital": "New Capital 1",
#           "Population": "123,456,789"},
#     "2": {"Country": "New Country 2",
#           "Capital": "New Capital 2",
#           "Population": "987,654,321"},
#     "3": {"Country": "New Country 3",
#           "Capital": "New Capital 3",
#           "Population": "111,222,333"}
# }

# df = pd.DataFrame.from_dict(countries, orient="index")

# print(df)


"""Nested Dictionary to Pandas DataFrame using Native Method"""

lst = [
    {
        "Student":[
            {"Exam":90,"Grade":"A"},
            {"Exam":80,"Grade":"B"},
            {"Exam":70,"Grade":"C"},
        ],
        "Name":"Misbah"
    },
    {
      "Student":[
            {"Exam":80,"Grade":"A"},
            {"Exam":70,"Grade":"B"},
            
        ],
        "Name":"Maadeha"   
    }
]

print(lst)


rows = []

for data in lst:

    data_row = data["Student"]
    time = data["Name"]
    for row in data_row:
        row['Name'] = time
        rows.append(row)

df2 = pd.DataFrame(rows)
print(df2)
df2 = df2.pivot_table(index='Name',columns="Grade",values="Exam").reset_index()
df2.columns = ['Name','Physic','Chemistry','Biology']
print(df2)








