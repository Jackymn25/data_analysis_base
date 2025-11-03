# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Case: A e-store user behaviour dataset is shown as follows,
finish the follwing Tasks:

- Compute each user's total consumption
- Identify the largest customer here
- Compute all users' avg consumption amount
- compute electronic products' total purchase volume
"""

data = {
    'UserId': [i for i in range(101, 106)],
    'Username': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'ProductType': ['Electronics', 'Cloths', 'Electronics', 'Furniture', 'Cloths'],
    'UnitPrice': [1200, 300, 800, 150, 200],
    'PurchaseVolume': [1, 3, 2, 5, 4]
}
df = pd.DataFrame(data)

# Task 1
df['TotalConsumption'] = df.UnitPrice * df.PurchaseVolume
print(df)

# Task 2
print(df.nlargest(1, columns=['TotalConsumption']))

# Task 3
print(df.TotalConsumption.mean().round(2))

# Task 4
print(df[df.ProductType == 'Electronics'].PurchaseVolume.sum())
