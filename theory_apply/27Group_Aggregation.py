# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# df.groupby('group')['aggregation']

df = pd.read_csv('data/employees_206.csv')

print(df['department_id'].isna().sum())

df.dropna(subset=['department_id'], inplace=True)

print(df['department_id'].isna().sum())

df['department_id'] = df['department_id'].astype('int64')

# Task 01 Compute each department's avg salary
print(df.groupby('department_id').groups)
# dict { department : index }
print(df.groupby('department_id').get_group(10))

# aggregation
print('\n\n')
print(df.groupby('department_id')['salary'].describe())

df2 = df.groupby('department_id')[['salary']].mean()
df2['salary'] = df2.salary.round(2)
print(df2)
df2.sort_values(by = 'salary', inplace=True)
print(df2)

# by department and job title
print(df.groupby(['department_id', 'job_id'])[['salary']].mean())
df3 = df.groupby(['department_id', 'job_id'])[['salary']].mean()
print(df3)
print(df3.sort_values(by = 'salary'))

df3 = df3.reset_index()
df3['salary'] = df3.salary.round(1)
print(df3)
