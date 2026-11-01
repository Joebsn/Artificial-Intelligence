# %% Imports
import pandas as pd
import numpy as np

# %% Pandas Series
data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print("Pandas Series:")
print(s)

# %% Pandas DataFrame
df = pd.DataFrame() 
print(df)
lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
df = pd.DataFrame(lst) 
print(df)

# %% Operations
df = pd.read_csv("data.csv")
print(df.head())

df.info()
# %%  Handling Missing Data
print(df.isnull().sum())
df = df.fillna(0) # replace missing values with 0

# %% Filter data
ages = df[df['age'] > 25]
print(ages)

# %% Adding and Removing Columns
df['total'] = df['a'] + df['b']
print(df.head())

# %% Grouping Data (GroupBy)
res = df.groupby('category')['sales'].sum()
print(res)
