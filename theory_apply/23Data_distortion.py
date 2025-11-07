
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = {
    "ID": [1,2],
    'Name': ['Alice', 'Bob'],
    'Math': [99, 83],
    'English': [88, 92],
    'Science': [86, 96]
}

df = pd.DataFrame(data)
print(df)
print(df.T)

# convert to record type
df2 = pd.melt(df, id_vars=['ID', 'Name'],
              var_name='Subjects',
              value_name='score')
print(df2)

print(df2.sort_values('Name'))
print('\n')
print('\n')
# reverse
df3 = pd.pivot(df2, index=['ID', 'Name'],
               columns='Subjects', values='score')
print(df3)

# data split columns
data = {
    "ID": [1,2],
    'Name': ['Alice Li', 'Bob Smith'],
    'Math': [99, 83],
    'English': [88, 92],
    'Science': [86, 96]
}
df = pd.DataFrame(data)

df[['firstName', 'lastName']] = df['Name'].str.split(" ", expand=True)
print(df)
