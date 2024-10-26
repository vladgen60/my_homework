    # ЗАДАНИЕ "РАЗ, ДВА, ТРИ, ЧЕТЫРЕ, ПЯТЬ".


def calculate_structure_sum(data_structure):    # Создаем функцию.
    total_sum = 0   # Создаем переменную равную нулю.
    for item in data_structure: # Перебираем все элементы аргумента функции.
        if isinstance(item, int):   # Если число, то прибавляем к нашей переменной.
            total_sum += item
        elif isinstance(item, str): # Если строка, то прибавляем к нашей переменной длину строки.
            total_sum += len(item)
        elif isinstance(item, list):    # Если список, то прибавляем к нашей переменной значение нашей функции.
            total_sum += calculate_structure_sum(item)  # т. е. рекурсия.
        elif isinstance(item, tuple):   # Если кортеж, то прибавляем к нашей переменной значение нашей функции.
            total_sum += calculate_structure_sum(item)  # т. е. рекурсия.
        elif isinstance(item, dict):    # Если словарь, то прибавляем к нашей переменной значение нашей функции.
            total_sum += calculate_structure_sum(list(item.keys())) # предварительно преобразовав ключи в список.
            total_sum += calculate_structure_sum(list(item.values()))   # предварительно преобразовав значения в список.
        elif isinstance(item, set): # Если множества,
            total_sum += calculate_structure_sum(item)  # то прибавляем к нашей переменной значение нашей функции.
    return total_sum    # Возвращаем значение

#           П Р И М Е Р


data_structure = [[1,2,3],{'a': 4, 'b': 5},(6, {'cube': 7,'drum':8}),"Hello",((),[{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)