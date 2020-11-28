from enum import Enum


class Industries(Enum):
    """ Анализируемые промышленные отрасли """
    COMMON = "COMMON"  # общая
    MINERAL = "MINERAL"  # полезные ископаемые
    PROCESS = "PROCESS"  # обработка
    UTILITIES = "UTILITIES"  # электричество-газ-вода
