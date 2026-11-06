
import pandas as pd


df = pd.read_csv(r"C:\Users\hdobh\python\project dehradun.py\housing_merged.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

print(df.columns)
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())


df[['Locality','City']] = df['Location'].str.split(',', expand=True)
print(df[['Locality','City']].head())
df.to_csv("cleaned_housing.csv", index=False)

print("Cleaned dataset saved successfully!")

print(df['City'].value_counts())
print(df['Status'].value_counts())

