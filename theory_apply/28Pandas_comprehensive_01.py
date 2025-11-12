# -*- coding: utf-8 -*-

# This is a dataset analysis of penguins
# Task 00: Import modules needed and read dataset
# Task 01: Clean dataset
# Task 02: Construct data features
# Task 03: Some data analysis

# Task 00
import pandas as pd
import numpy as np

df = pd.read_csv('other_data/penguins.csv')
print(df.head(3))
print(df.info())

# Task 01
# check missing value
print(df.isna().sum())

# drop missing values
df.dropna(inplace=True)

# verify this works
print(df.isna().sum())

print(len(df))

# Task 02
df['sex'] = df['sex'].astype('category')
df['bill_ratio'] = df['bill_length_mm'] / df['bill_depth_mm']

# Task 03
# partitioning weight into 3 levels
labels = ['low', 'medium', 'high']

df['weight_level'] = pd.cut(df['body_mass_g'],
                            bins=3,
                            labels=labels)
print(df.head())

print(df['weight_level'].value_counts())

# analyze mean sample of female male
print(df.groupby(['sex']).agg({
    'body_mass_g' : ['mean', 'count']
}))

# analyze mean sample of island origins
print(df.groupby(['island']).agg({
    'body_mass_g' : ['mean', 'count']
}))
