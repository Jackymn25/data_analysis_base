# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Recall: series/df.isnull() .isna()

# example
df = pd.DataFrame([[1,2,pd.NA,9],[2, None, 3,9], [np.nan, 4, np.nan,9],
                   [1,2,3,4],
                   [np.nan, np.nan, np.nan,np.nan],
                   [np.nan, 4, np.nan, None]])

print(df.isna())
print(df.isna().sum())
print(df.isna().sum(axis=1))

# drop na
print(df)
# delete all row data with a na
print(df.dropna())

print(df.dropna(how='all'))
print(df.dropna(thresh=2)) # if two values or more is vaLid, keep data

print(df.dropna(axis=1))

print(df.dropna(subset=[1]))

print(df.fillna({2:9999}))
print(df.fillna(df[[2]].mean()))

print(df)
print(df.ffill())
print(df.bfill())
