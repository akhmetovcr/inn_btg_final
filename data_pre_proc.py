import numpy as np
import datetime as dt
import pandas as pd
import unittest


# Сглаживание скользящим средним
def running_mean(y: np.ndarray, window: int) -> np.ndarray:
    yc = np.pad(y, window, mode='symmetric')
    yy = y.copy()
    for wi in range(window, len(y) + window):
        yy[wi - window] = np.nanmean(yc[wi - window: wi + window])

    return yy


# фильтруем по датам
def filter_by_date(data_frame: pd.DataFrame, date_from: dt.datetime, date_to: dt.datetime):

    return (date_from <= data_frame.index) & (data_frame.index <= date_to)


class MyTestCase(unittest.TestCase):

    def test_filter(self):
        df = pd.DataFrame(np.arange(12).reshape(3, 4), index=[dt.datetime(2020, 10, day) for day in range(1, 4)])
        df = df[filter_by_date(df, dt.datetime(2020, 10, 1), dt.datetime(2020, 10, 2))]
        print(df)
