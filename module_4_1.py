    # Модуль module_4_1

from fake_math import divide as fake_divide # Импортируем из модуля fake_math функцию divide с переназначением имени.
from true_math import divide as true_divide # Импортируем из модуля true_math функцию divide с переназначением имени.

    # ПРИМЕРЫ РАБОТЫ ИМПОРТИРОВАНЫХ ФУНКЦИЙ.
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)