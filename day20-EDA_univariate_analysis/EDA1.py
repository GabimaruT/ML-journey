import pandas as pd 
df = pd.read_csv('Titanic-Dataset.csv')

# 1. How big s the data ?
print(df.shape)

# 2. How dose a data looks like ?
print(df.sample(5))  # gives random 5  rows 

# 3. What is the data type of column ?
print(df.info())

# 4. Are their any messing values ?
print(df.isnull().sum())

# 5. How dose data looks mathematically ?
print(df.describe())

# 6. Are their duplicate values ?
print(df.duplicated().sum())

# 7. How is the collection between colums ?
print(df.corr(numeric_only=True))