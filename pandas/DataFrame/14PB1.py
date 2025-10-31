# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

data = pd.read_csv("student_performance__preview_.csv")
print(data.head())

#Q1
df = data
# peremetres of class in pd
print(df.shape)
print(df.ndim)
print(df.size)

print(df.index.tolist()) # row0 - 12
print(df.columns.tolist()) # column stu......

print(df.dtypes) # name class city are objects(string) some data are in float, and date is object, pass status is bool

# Q2
# 5)
id = df['student_id']
name = df.name
class_ = df.loc[:, ['class']]
math = df.iloc[:, 4]

print(id, name, class_, math, sep = '\n\n')

# 6)
sub_data = df[(df['class'] == 'A') & (df.math >= 80)]
print(sub_data)

# 7) data cleaning
sub_data = df[(df.city == 'Shanghai')]
print(sub_data)
print(sub_data.shape[0])

mask_shanghai = (
    df["city"]
    .astype(str)
    .str.strip()
    .str.casefold()
    .eq("shanghai")
)

df_shanghai = df.loc[mask_shanghai].copy()
print("Shanghai row(cleaning condition passed): ", mask_shanghai.sum())
print(mask_shanghai, df_shanghai)

df_shanghai.to_csv("student_shanghai_only.csv", index=False, encoding="utf-8-sig")

# cleaning
df["city"] = (
    df["city"]
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title() # -> Shanghai
)

print(df)
