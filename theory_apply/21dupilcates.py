# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = {
    'name': ['Alice', 'Alice', 'alice', 'Bob', 'jack','Alice', ' alice '],
    "age": [26, 25, 26, 30, 77, 26, 27],
    'city': ['NY', 'NY', 'NY','LA', 'SF', 'NY', 'NY']
}
df = pd.DataFrame(data)

# Task 00
df["name"] = (
    df["name"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title() # alice -> Alice
)
print(df)

# Task 01
print(df)
print(df.duplicated())
print(df.drop_duplicates())
df = df.drop_duplicates()

# Task 02
print(df.drop_duplicates(subset=['name'], keep='last'))
