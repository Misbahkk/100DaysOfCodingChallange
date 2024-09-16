import pandas as pd

# 
df = pd.read_csv('visitors.csv')
print(df.columns)
# convert the appt_start_date column in datetime because this 
# column we hav estring so we convert the data type


df['appt_start_date'] = pd.to_datetime(df['appt_start_date'])
print(df['appt_start_date'])

# convert appt_end_date into datetime
df['appt_end_date'] = pd.to_datetime(df['appt_end_date'])

# check tht in which day we get more meetings
date_month = df['appt_start_date'].dt.strftime("%B-%Y")
print(date_month.value_counts())


meeting_duration =df['appt_end_date'] -df['appt_start_date']
# Maximum duration of meeting 
print(meeting_duration.max())
# minimum duration of meeting
print(meeting_duration.min())
# sum of all meeting times
print(meeting_duration.value_counts().sum())


