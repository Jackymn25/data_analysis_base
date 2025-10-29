# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Given a sales data (per hour) of a store
# - convert data to per day
# - compute ratio between running hours(8-22) to non-running horus
# - find the most profitable 3 hours

np.random.seed(42)
hourly_sales = pd.Series(np.random.randint(0, 100, 24),  # 0 - 99
                         index = pd.date_range('2025-01-01',
                                               periods = 24,
                                               freq = 'h'))
print(hourly_sales)

# - convert data to per day
data = hourly_sales.resample('D')
# resample returns a Resampler Object
print(data.sum())

# - compute ratio between running hours(8-22) to non-running horus
running = hourly_sales[(hourly_sales.index.hour >= 8) & (hourly_sales.index.hour <= 22)]
nonrunning = hourly_sales[(hourly_sales.index.hour < 8) | (hourly_sales.index.hour > 22)]

sum1 = running.sum()
sum2 = nonrunning.sum()
print(sum1/sum2)

# alternative way
sales_8_22 = hourly_sales.between_time('8:00', '22:00', inclusive='both')
other = hourly_sales.drop(sales_8_22.index)

# - find the most profitable 3 hours
print(hourly_sales.nlargest(3))

# additional - find the most profitable(continous) 3-hour
data = hourly_sales.rolling(3).sum()

end_t = data.idxmax()

start_t = end_t - pd.Timedelta(hours=2)

print(data, start_t, end_t, sep = '\n')
