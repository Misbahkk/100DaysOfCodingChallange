# Collapse multiple Columns in Pandas

import pandas as pd


# data= {
#     'sample_n' :['S1','S2','S3'],
#     'Sample_1' : [57, 51, 6] ,
#     'Sample_2' : [92, 16, 19], 
#     'Sample_3' : [15, 93, 71], 
#     'Sample_4' : [28, 73, 31]
# }
data={
    'sample_n' :['S1','S2','S3'],
    'Sample_1' : ['57', '51', '6'] ,
    'Sample_2' : ['92', '16', '19'], 
    'Sample_3' : ['15', '93', '71'], 
    'Sample_4' : ['28', '73', '31']
}

df = pd.DataFrame(data)
print(df)
mapping = {'sample_1':'Result_1','sample_2':'Result_1','sample_3':'Result_2','sample_4':'Result_2'}


df2= df.set_index('sample_n').groupby(mapping,axis=1).sum()
print(df2.reset_index(level=0))