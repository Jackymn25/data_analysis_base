# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Case: A sales dataset of a company is shown as follows,
finish the follwing Tasks:

- compute each product's total sales figure
- find the most profitable product
- rank sales figure from high to low, output all product info
- 
"""

data = {
    'Product Name': ['A', 'B', 'C', 'D'],
    'Unit Price': [100, 150, 200, 120],
    'Sales Volume': [50, 30, 20, 40]
}

df = pd.DataFrame(data)
print(df.head())

# Task 1
df['Total Profit'] = df['Unit Price'] * df["Sales Volume"]
print(df['Total Profit'])
print(df.head())

# Task 2
print(df.sort_values(by='Total Profit')["Product Name"][0])
print(df.nlargest(1,columns=['Total Profit']))

# Task 3
print(df.sort_values(by='Total Profit', ascending = False))
