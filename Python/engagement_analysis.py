
import pandas as pd

df = pd.read_csv('user_engagement_data.csv')

dau = df.groupby('Date')['UserID'].nunique()
avg_session = df.groupby('Date')['SessionDuration'].mean()

print("DAU:")
print(dau.head())

print("\nAverage Session Duration:")
print(avg_session.head())
