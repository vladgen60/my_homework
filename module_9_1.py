# "Вызов разом"
 
def apply_all_func(int_list, *functions): # Создаем функцию apply_all_func(int_list, *functions).
    results = {}
    for func in functions:  # Перебераем все функции из *functions.
        results[func.__name__] = func(int_list) # Записываем в словарь results в качестве ключа её названия, а в качестве значения ее работу. 
    return results

    # П Р И М Е Р Ы

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))