from enum import Enum


COUNTRY = "Российская Федерация"


class Districts(Enum):
    VOLGA = "Приволжский федеральный округ"
    URAL = "Уральский федеральный округ"


class Region(Enum):
    """ Регионы """
    Bash = "Республика Башкортостан"
    Oren = "Оренбургская область"
    Perm = "Пермский край"
    Sverd = "Свердловская область"
    Tymen = "Тюменская область"
    Chel = "Челябинская область"


# Названия регионов
URAL_FILE_NAMES = {
    Region.Bash: 'Республика_Башкортостан.csv',
    Region.Oren: 'Оренбургская_область.csv',
    Region.Perm: 'Пермский_край.csv',
    Region.Sverd: 'Свердловская_область.csv',
    Region.Tymen: 'Тюменская_область.csv',
    Region.Chel: 'Челябинская_область.csv',
}
