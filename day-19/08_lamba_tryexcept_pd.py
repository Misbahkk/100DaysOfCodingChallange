# import pandas as pd 

# mod_df = pd.read_csv("clean_modern_arts.csv")

# # Select retweets from the mos_df  DataFrame: result
# result = filter(lambda x:x[0:3]=="Eug",mod_df["Artist"])
# res_list = list(result)
# for artist in res_list:
#     print(artist)

x = ['cry', 'myth', 'aqua', 'ciao']
n_vowel = map(lambda 
w:
 w.count('a'), x)
print(list(n_vowel))
