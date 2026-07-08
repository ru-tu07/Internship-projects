import pandas as pd

data = pd.read_csv("mtcars(1).csv")

print("Complete Dataset")
print(data)

print("\nFirst 5 Rows:")
print(data.head())

print("\nLast 5 Rows:")
print(data.tail())

print("\nDataset Information:")
data.info()

print("\nStatistical Summary:")
print(data.describe())

print("\nColumn Names:")
print(data.columns)

print("\nShape of Dataset:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nData Sorted by MPG:")
print(data.sort_values("mpg"))

print("\nGear Count:")
print(data["gear"].value_counts())

print("\nAverage MPG:")
print(data["mpg"].mean())