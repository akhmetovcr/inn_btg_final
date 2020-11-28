from data.regions import Region
from data.industry import Industries


# Названия папок по регионам
YEAR_DATA_REGION_FOLDER_NAME_MAP = {
    Region.Bash: 'bashkortostan',
    Region.Chel: 'chelyabinsk',
    Region.Oren: 'orenburg',
    Region.Perm: 'perm',
    Region.Sverd: 'sverdlovsk',
    Region.Tymen: 'tumen'
}


# названия файлов с данными по отраслям
YEAR_DATA_INDUSTRY_NAME_MAP = {
    Industries.COMMON: 'общее.txt',
    Industries.MINERAL: 'ископаемые.txt',
    Industries.PROCESS: 'обрабатывающие.txt',
    Industries.UTILITIES: 'электроэнергия-газ-вода.txt',
}


# названия месяцев
YEAR_DATA_MONTH_RU = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                      "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

# данные для каких годов
YEAR_VOLUMES = range(2016, 2021)
