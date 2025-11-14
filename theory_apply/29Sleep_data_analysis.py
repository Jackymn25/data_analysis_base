# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('other_data/sleep.csv')
print(df.head(), df.info(), sep = '\n')

print(df.describe())

# clean dataset
print(df.isna().sum())

print(df['sleep_disorder'].value_counts())

# df.drop(column='sleep_disorder', inplace=True) not recommended as there's 209 data dropped
df['gender'] = df.gender.astype('category')
df['occupation'] = df.occupation.astype('category')
df['bmi_category'] = df.bmi_category.astype('category')
df[['high','low']] = (df['blood_pressure'].str
                                          .split('/',
                                                 expand=True))

print(df.head())

# partitioning
labels = ['good', 'medium', 'bad']
df['quality_level'] = pd.cut(df['sleep_quality'],
       bins=3,
       labels=labels)

age_labels = ['Teen', 'Middle_aged', 'Elderly']
df['age_level'] = pd.cut(df['sleep_quality'],
       bins=3,
       labels=age_labels)

print(df.head())

# stats, analysis
print(df['bmi_category'].value_counts())

# groupby bmi
print(df.groupby(['age_level','bmi_category']).agg({
    'sleep_duration': 'mean',
    'sleep_quality': 'mean',
    'stress_level': 'mean'
}))
