# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('data/employees_100.csv')
print(df.head(10))

df1 = df.head(10)[['employee_id', 'salary']]
print(df1)

# cut into 3 groups by salary values
print(pd.cut(df1['salary'], bins=3))

print(pd.cut(df1['salary'], bins=3).value_counts())

# cut into 3 groups by customized range
print(pd.cut(df1['salary'],
             bins=[0,10000,20000,30000]).value_counts())

# labels
df1['Salary_level'] = pd.cut(df1['salary'],
             bins=[0,10000,20000,30000], labels=['low', 'medium', 'high'])

print(df1)
# category is faster!
print(df1.Salary_level.dtype)

# qcut cut through number of elements not values
print(pd.qcut(df1['salary'],3).value_counts())

# utils rename set_index reset_index

df = pd.DataFrame({
    'name' : ['jack', 'Peter', 'Alice', 'Mick'],
    'age' : [19, 20, 29, 38],
    'gender': ['M','M','F','M']
})

df['gender'] = df.gender.astype('category')

# example 1
print(np.linspace(1,4, 4, dtype=int))
print(df.set_index(np.linspace(1,4, 4, dtype=int)))

# example 2
df.set_index('name',inplace=True)
print(df)

# reset
df.reset_index(inplace=True)
print(df)

# rename age -> Age index 0 -> index 4
print(df.rename(columns={'age':'Age'},
                index={0:4}))

# alternative way
df.index = np.arange(1,5,1)
df.columns = ['姓名', '年龄', '性别']
print(df)
