import pandas as pd

df = pd.read_csv("cleaned_marketing_campaign.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
