# Given a stock data of 10 days
# - calculate each day's profit rate
# - find the day with highest profit rate and lowest
# - rate of flowing

import numpy as np
import pandas as pd

# test case data -----------------------------------------------------
PRICES = pd.Series([102.3, 103.5, 105.1, 104.8, 106.2,
                    107.0, 106.5, 108.1, 109.3, 110.2],
                   index = pd.date_range('2025-01-01', periods=10))
# --------------------------------------------------------------------

# print(prices.index)

def profit_rate(p_data: pd.Series) -> pd.Series:
    """
    :param p_data:
    :return:

    >>> profit_rate(PRICES).iat[0]
    np.float64(nan)
    >>> profit_rate(PRICES).iat[1]
    np.float64(0.011730205278592365)
    """
    return p_data.pct_change()

def high_low_day(p_data: pd.Series) -> tuple[str, str]:
    """
    :param p_data:
    :return:
    """
    return profit_rate(p_data).idxmax(), profit_rate(p_data).idxmin()

def flow_rate(p_data: pd.Series) -> float:
    """
    :param p_data:
    :return:
    """
    return profit_rate(p_data).std()


if __name__ == '__main__':
    print(profit_rate(PRICES))

    print(high_low_day(PRICES))

    print(flow_rate(PRICES))
