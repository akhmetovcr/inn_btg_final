import os
import pandas as pd
import numpy as np
import datetime as dt

from data.industry import Industries
from data.regions import SysID, SYS_REGIONS
from data.src_data_industry.year_data_map import YEAR_DATA_INDUSTRY_NAME_MAP, YEAR_DATA_REGION_FOLDER_NAME_MAP, \
    YEAR_DATA_MONTH_RU, YEAR_VOLUMES


def parse_industry_volume(file_name, volume_name):
    """ Парсим данные с файла """

    # dates = [dt.date(year, month, day=1) for month in range(1, 13) for year in YEAR_VOLUMES]
    industry_df = pd.DataFrame(columns=[volume_name])
    # прочитали
    json_df = pd.read_json(file_name)
    for month_ind, month in enumerate(range(1, 13)):
        # даты
        dates = np.array([dt.date(year, month, day=1) for year in YEAR_VOLUMES])
        # значения
        volumes = json_df['data'][month_ind][1:]

        # фильтруем от None
        filter_v = []
        filter_d = []
        for v, d in zip(volumes, dates):
            if v is not None:
                filter_v.append(v)
                filter_d.append(d)
        volumes = filter_v
        dates = filter_d

        month_volumes = pd.DataFrame(volumes,
                                     columns=[volume_name],
                                     index=dates)
        # industry_df = pd.concat([industry_df, month_volumes])
        # industry_df[dates] = month_volumes
        industry_df = pd.DataFrame.append(industry_df, month_volumes)

    # пересчитаем данные не как накопительные
    industry_df = industry_df.sort_index()

    # необходимо найти разности соседних значений
    for year in YEAR_VOLUMES:
        start_date = dt.date(year, 1, 1)
        before_value = industry_df.loc[start_date]
        for month in range(2, 13):
            cur_date = dt.date(year, month, 1)
            # в текущий день уменьшаем на значение предыдущего
            if cur_date in industry_df.index:
                industry_df.loc[cur_date] -= before_value
                before_value += industry_df.loc[cur_date]

    return industry_df


def parse_region_industry_volume(path):
    """ Парсим данные по региону """
    # месяц и столбцы по каждой отрасли
    region_df = pd.DataFrame()
    for industry in Industries:
        # название файла данных по отраслям
        file_name = os.path.join(path, YEAR_DATA_INDUSTRY_NAME_MAP[industry])
        # получаем данные по отрасли
        industry_volume_df = parse_industry_volume(file_name, industry.value)
        # объединяем в одну таблицу
        region_df = pd.concat([region_df, industry_volume_df], axis=1)

    return region_df


# объединенные данные по ОЭС
def calc_sys_industry_volume(path, sys: SysID):
    # общие данные
    sys_volume = pd.DataFrame()

    for region in SYS_REGIONS[sys]:
        region_df = parse_region_industry_volume(os.path.join(path, YEAR_DATA_REGION_FOLDER_NAME_MAP[region]))

        sys_volume = sys_volume.add(region_df, fill_value=0)

    return sys_volume


# объемы по уральской зоне
URAL_SYS_INDUSTRY_VOLUME = calc_sys_industry_volume(os.path.join('data', 'src_data_industry'), SysID.URAL)


if __name__ == '__main__':
    # print(parse_industry_volume(os.path.join('data', 'src_data_industry', 'bashkortostan', 'общее.txt'), Industries.COMMON.value))
    # print(parse_region_industry_volume(os.path.join('data', 'src_data_industry', 'bashkortostan')))
    print(calc_sys_industry_volume(os.path.join('data', 'src_data_industry'), SysID.URAL))
