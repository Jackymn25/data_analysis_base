# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import unittest

# Given a sales number data of past 12 months
# - Compute each season's average sales amount
# - Compute month over month increase rate
# - Find the month which has continous increase for over 2 months

sales = pd.Series([120, 135, 145, 160, 155,
                   170, 180, 175, 190, 200,
                   210, 220],
                  index = pd.date_range('2025-01-01',
                                        periods = 12,
                                        freq = 'M'))

# - Compute each season's average sales amount
res = sales.resample("QS").mean()
print(res)

# Alternative way
res = sales.resample("3MS").mean()
print(res)

# - Compute month over month increase rate
res = sales.pct_change()
print(res)

# increasement
res = sales.diff()
print(res)

# - Find the month which has continous increase for over 2 months
pct_change = sales.pct_change()
bool = pct_change > 0
window = bool[bool.rolling(3).sum() == 3].keys().tolist()
print(window)


s1 = pd.Series([1, 2, 3], index = [0, 1, 2])
print(s1)

print(s1[s1 == 3].keys().tolist()[0])
print(s1.index[s1.eq(3)])
