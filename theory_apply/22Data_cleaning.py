# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv("data/students_messy_127.csv")
print(df.head())

df.gender = df['gender'].astype('category')
print(df.gender.dtypes)

df.name = (
    df.name
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

print(df)
