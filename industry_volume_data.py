import os
import pandas as pd
import datetime as dt

from data.industry import Industries
from data.src_data_industry.year_data_map import YEAR_DATA_INDUSTRY_NAME_MAP, YEAR_DATA_REGION_FOLDER_NAME_MAP, \
    YEAR_DATA_MONTH_RU, YEAR_VOLUMES


def parse_industry_volume(file_name, volume_name):
    """ Парсим данные с файла """
    industry_df = pd.DataFrame(columns=['DATE', volume_name])
    # прочитали
    json_df = pd.read_json(file_name)
    for month_ind, month in enumerate(range(1, 13)):
        # даты
        dates = [dt.date(year, month, day=1) for year in YEAR_VOLUMES]
        # значения
        volumes = json_df['data'][month_ind][1:]
        month_volumes = pd.DataFrame(zip(dates, volumes),
                                     columns=['DATE', volume_name])
        industry_df = pd.concat([industry_df, month_volumes])

    return industry_df


def parse_region_industry_volume(path):
    """ Парсим данные по региону """
    # месяц и столбцы по каждой отрасли
    region_df = None
    for industry in Industries:
        # название файла данных по отраслям
        file_name = os.path.join(path, YEAR_DATA_INDUSTRY_NAME_MAP[industry])
        # получаем данные по отрасли
        industry_volume_df = parse_industry_volume(file_name, industry.value)
        # объединяем в одну таблицу
        if region_df is None:
            region_df = industry_volume_df
        else:
            region_df = region_df.merge(industry_volume_df, on="DATE")

    return region_df


# данные по регионам
REGION_VOLUMES = {}
for region, folder in YEAR_DATA_REGION_FOLDER_NAME_MAP.items():
    REGION_VOLUMES[region] = parse_region_industry_volume(os.path.join('data', 'src_data_industry', folder))


if __name__ == '__main__':
    print(REGION_VOLUMES)
