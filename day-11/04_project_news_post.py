import pandas as pd
# 
# 
## add the CSV file
news_df = pd.read_csv('practice on youtube vedio\hacks.csv')
print(news_df.columns)

#  firstly we check the konse post pa sb sa zyda comment ata "ask hn" or "show hn"

# this line give a boolen series of titele where ask hn that it show true
ask_bol = news_df["title"].str.lower().str.startswith("ask hn")
ask_posts = news_df[ask_bol]

# Now crete the another dataframe for "show hn"
show_bol = news_df["title"].str.lower().str.startswith('show hn')
show_posts = news_df[show_bol]

# Now we check that which post have maximum comments
ask_posts['num_comments']
ask_commit = ask_posts['num_comments'].mean()

show_commit =show_posts['num_comments'].mean()
print(f'Ask post have {ask_commit} and Show posts have {show_commit}')

# convert the datetime into real formated
ask_posts['created_at']=pd.to_datetime(ask_posts['created_at']).copy()

ask_posts['hour'] =ask_posts['created_at'].dt.hour
# check that in which time the most of commit
avg_commits_ask_post = ask_posts.pivot_table(index='hour' , values='num_comments').sort_values('num_comments', ascending=False)
print(avg_commits_ask_post.head(5))


# now crete the another hour colium in show hn posts 
show_posts['created_at'] =pd.to_datetime(show_posts['created_at'])
show_posts['Hour'] = show_posts['created_at'].dt.hour

#  check that in which time of most comment
avg_comment_show_post = show_posts.pivot_table(index='Hour',values='num_comments').sort_values('num_comments',ascending= False)

print(avg_comment_show_post.head(5))
