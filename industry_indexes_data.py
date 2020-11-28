
# необходимые либы
import pandas as pd
import datetime as dt
import os

from data.regions import URAL_FILE_NAMES, Districts, COUNTRY


def date_parser(period):
    period = period.replace('январь-', '')
    period = period.replace(' года', '')
    month_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь', ]
    for month, month_ru in enumerate(month_ru, 1):
        period = period.replace(month_ru, str(month))

    # останется в формате "3 2020"
    return dt.datetime.strptime(period, '%m %Y')


def get_data_frame_by_path(path) -> pd.DataFrame:
    df = None

    # импортируем Уральские файлы
    for region, fn in URAL_FILE_NAMES.items():
        region_df = pd.read_csv(os.path.join(path, 'Ural', fn),
                                sep=',', encoding="cp1251",
                                parse_dates={'DATE': ['Период']},
                                date_parser=date_parser)
        # удаляем столбец данных страны
        region_df = region_df.drop(columns=[COUNTRY])
        # удаляем столбец данных округа
        for distr in Districts:
            if distr.value in region_df.keys():
                region_df = region_df.drop(columns=[distr.value])

        # объединяем в один массив
        if df is None:
            df = region_df
        else:
            df = df.merge(region_df, on='DATE')

        # столбец DATE записываем в индексы
        df.index = df['DATE']
        df = df.drop(columns=['DATE'])

    return df


# Парсим файлы в датафреймы
BUILD_WORK_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'build_works', 'month'))
IPM_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'ipm', 'month'))
IPM_FARM_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'ipm_farm', 'month'))
OPT_ORG_TRADE_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'opt_org_trade', 'month'))
RETAIL_TRADE_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'retail_trade', 'month'))
TRADE_EXPORT_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'trade_export', 'month'))
TRADE_IMPORT_DF = get_data_frame_by_path(os.path.join('data', 'industrial_indexes', 'trade_import', 'month'))


if __name__ == '__main__':
    for df in [BUILD_WORK_DF, IPM_DF, IPM_FARM_DF, OPT_ORG_TRADE_DF, RETAIL_TRADE_DF, TRADE_EXPORT_DF]:
        print(df)
