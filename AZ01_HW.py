import pandas as pd

df = pd.read_csv("world-data-2023.csv")

print(df.head())
print(df.info())
print(df.describe())


df = pd.read_csv('dz.csv')

print(df.groupby('City')['Salary'].mean())