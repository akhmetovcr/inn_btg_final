from enum import Enum


COUNTRY = "Российская Федерация"


class Districts(Enum):
    VOLGA = "Приволжский федеральный округ"
    URAL = "Уральский федеральный округ"


class SysID(Enum):
    """ Идентификаторы ОЭС по данным сайта br.so-ups.ru """
    URAL = 630000


class Region(Enum):
    """ Регионы """
    Bash = "Республика Башкортостан"
    Oren = "Оренбургская область"
    Perm = "Пермский край"
    Sverd = "Свердловская область"
    Tymen = "Тюменская область"
    Chel = "Челябинская область"


# список регионов по ОЭС
SYS_REGIONS = {
    SysID.URAL: [Region.Bash, Region.Oren, Region.Perm, Region.Sverd, Region.Tymen, Region.Chel]
}

# Названия регионов
URAL_FILE_NAMES = {
    Region.Bash: 'Республика_Башкортостан.csv',
    Region.Oren: 'Оренбургская_область.csv',
    Region.Perm: 'Пермский_край.csv',
    Region.Sverd: 'Свердловская_область.csv',
    Region.Tymen: 'Тюменская_область.csv',
    Region.Chel: 'Челябинская_область.csv',
}
