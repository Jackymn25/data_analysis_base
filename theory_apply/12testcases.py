# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import unittest

def make_sales_series():
    # Given a sales number data of past 12 months
    sales = pd.Series([120, 135, 145, 160, 155,
                       170, 180, 175, 190, 200,
                       210, 220],
                      index=pd.date_range('2025-01-01',
                                          periods=12,
                                          freq='M'))
    return sales


# - Compute each season's average sales amount
def season_avg_qs(sales):
    res = sales.resample("QS").mean()
    return res


# Alternative way
def season_avg_3ms(sales):
    res = sales.resample("3MS").mean()
    return res


# - Compute month over month increase rate
def mom_pct_change(sales):
    res = sales.pct_change()
    return res


# increasement
def mom_diff(sales):
    res = sales.diff()
    return res


# - Find the month which has continous increase for over 2 months
def find_continuous_increase_over_2_months(sales):
    pct_change = sales.pct_change()
    bool = pct_change > 0
    window = bool[bool.rolling(3).sum() == 3].keys().tolist()
    return window



class TestSalesCalculations(unittest.TestCase):
    def setUp(self):
        self.sales = make_sales_series()

    def test_season_avg_qs(self):
        res = season_avg_qs(self.sales)
        # Q1: Jan–Mar
        self.assertAlmostEqual(
            res.loc[pd.Timestamp("2025-01-01")],
            (120 + 135 + 145) / 3.0, places=7
        )
        # Q2: Apr–Jun
        self.assertAlmostEqual(
            res.loc[pd.Timestamp("2025-04-01")],
            (160 + 155 + 170) / 3.0, places=7
        )
        # Q3: Jul–Sep
        self.assertAlmostEqual(
            res.loc[pd.Timestamp("2025-07-01")],
            (180 + 175 + 190) / 3.0, places=7
        )
        # Q4: Oct–Dec
        self.assertAlmostEqual(
            res.loc[pd.Timestamp("2025-10-01")],
            (200 + 210 + 220) / 3.0, places=7
        )

    def test_mom_pct_change(self):
        res = mom_pct_change(self.sales)
        # 2025-02 vs 2025-01: (135-120)/120 = 0.125
        self.assertAlmostEqual(res.loc[pd.Timestamp("2025-02-28")], 0.125, places=7)
        # 2025-03 vs 2025-02: (145-135)/135
        self.assertAlmostEqual(res.loc[pd.Timestamp("2025-03-31")], 10/135, places=7)
        # 2025-05 vs 2025-04: (155-160)/160
        self.assertAlmostEqual(res.loc[pd.Timestamp("2025-05-31")], -5/160, places=7)

    def test_mom_diff(self):
        res = mom_diff(self.sales)
        self.assertTrue(np.isnan(res.loc[pd.Timestamp("2025-01-31")]))
        self.assertEqual(res.loc[pd.Timestamp("2025-02-28")], 15)   # 135 - 120
        self.assertEqual(res.loc[pd.Timestamp("2025-05-31")], -5)    # 155 - 160
        self.assertEqual(res.loc[pd.Timestamp("2025-12-31")], 10)   # 220 - 210

    def test_find_continuous_increase_over_2_months(self):
        window = find_continuous_increase_over_2_months(self.sales)
        expected = [
            pd.Timestamp("2025-04-30"),
            pd.Timestamp("2025-11-30"),
            pd.Timestamp("2025-12-31"),
        ]
        self.assertEqual(window, expected)

if __name__ == "__main__":
    unittest.main()
