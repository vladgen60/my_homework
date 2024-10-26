 # Создание модуля true_math.py
from math import inf    # Импорт бесконечности из библиотеки math.
def divide(first, second):  # Создание функции.
    if second == 0: # Условие при котором
        return inf  # возвращается бесконечность.
    else:
        return first / second   # Возвращаем результат деления.