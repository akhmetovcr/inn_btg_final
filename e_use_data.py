import pandas as pd
import datetime as dt
from data.regions import SysID


# Объединяем колонки INTERVAL и M_DATE
def date_time_parser(d, t):
    date = dt.datetime.strptime(d, '%d.%m.%Y %H:%M:%S')
    try:
        hour = int(t)
    except ValueError:
        hour = 0
    time = dt.time(hour)
    return dt.datetime.combine(date, time)


def parse_e_use_df(fn, sys_id: SysID):
    """
    Парсим
    :param fn: название файла
    :param sys_id: идентификатор ОЭС
    :return: DataFrame
    """
    df = pd.read_csv(fn, usecols=['M_DATE', 'INTERVAL', 'E_USE_FACT', 'POWER_SYS_ID'],
                     sep=';', parse_dates={'DATE_TIME': ['M_DATE', "INTERVAL"]},
                     date_parser=date_time_parser)

    # Удалим неопределенные? зоны
    df = df[df['POWER_SYS_ID'] != 0]
    # фильтруем по ОЭС
    df = df[df['POWER_SYS_ID'] == sys_id.value]
    return df


if __name__ == '__main__':
    df = parse_e_use_df('data/2014_2020.csv', SysID.URAL)
    print(df)
