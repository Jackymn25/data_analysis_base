# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

d = pd.Timestamp('2015-05-02 10:23')
print(d, type(d), sep = '   ')
print(d.year, d.month, d.day, d.hour, d.second)

print(d.quarter) # season

print(d.day_name())

# -----------------------------------------------
d1 = pd.Timestamp('2015-05-02 10:23')
print(d1.to_period("D")) # Q Y M W
print(d1.to_period("W"))

# String to datetime
time_data = pd.to_datetime('20150730')
print(time_data)
print(time_data.day_name())

# df to datetime
df = pd.DataFrame({
    'sales': np.arange(100,301,100),
    'date': ['20250601', '20250602', '20250603']
})

df['datetime'] = pd.to_datetime(df.date)
print(df.info())
print(df)

print(df.datetime
        .dt
        .year
      )

# example
df = pd.read_csv('data/weather_sim_1000.csv')
print(df.head(3))
df['datetime'] = pd.to_datetime(df.date)
print(df.info())

print(df['datetime'].dt.day_name())

# alternative
df_ = pd.read_csv('data/weather_sim_1000.csv', parse_dates = ['date'])
print(df_.info())

# date as index
df.set_index('date', inplace=True)
print(df)

# slicing dates
print(df.loc['2018-01':'2018-02'])

# time interval
d1 = pd.Timestamp('20130115')
d2 = pd.Timestamp('20260929')
d3 = d2-d1
print(d3)

# example of use
df = pd.read_csv('data/weather_sim_1000.csv', parse_dates = ['date'])
print(df_.info())
df['delta'] = df['date'] - df['date'].iloc[0]
df.set_index('delta', inplace=True)
print(df)

print(df.loc['10 days': '40 days'])

# craeting data
days = pd.date_range('2025-07-03','20270901', freq='W')
days_ = pd.date_range('2025-07-03',periods=10, freq='W')
print(days, days_, sep ='\n\n')

# resample
df.set_index('date', inplace=True)
print(df.info())
print(df[['temp_min_C','temp_max_C']].resample('YE').mean())
