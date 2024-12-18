    # Р А С П А К О В К А
def print_params(a = 1, b = 'строка', c = True): # Определяем функцию print_params(), с тремя именнованными аргументами.
    print(a,b,c)
print_params()  # Выводим на экран значения аргументов по умолчанию.
#print_params(a = 1, b = 'строка', c = True, d = 4) # Вывод на экран значений с заданием количества аргументов не соответствующих количеству
# аргументв в функции, поэтому будет выдаваться ошибка и поэтому эта строка закоментированна.
print_params(c = False) # Вывод на экран с одним параметром "с" и его переназначением.
print_params(b = 25) # Вывод на экран с одним параметром "b" и его переназначением.
print_params(c = [1,2,3]) # Вывод на экран с одним параметром "с" и его переназначением.

    # Р A С П А К О В К А   П А Р А М Е Т Р О В

values_list = [2, 'запятая', [1,2,3]] # Создаем список с тремя значениями.
values_dict = {'a':5, 'b':'строка', 'c':False}    # Создаем словарь с тремя ключами и их значениями.
print_params(*values_list) # Проверяем функцию со значениями списка values_list.
print_params(**values_dict) # Проверяем функцию со значениями словаря values_dict.
values_list = [2, 'запятая', [1,2,3], 4.0] # Создаем список с 4-мя значениями.
values_dict = {'a':5, 'b':'строка'}    # Создаем словарь с 2-мя ключами и их значениями.
#print_params(*values_list) # Проверяем функцию со значениями списка values_list, не работает т. к. количество значений больше нежели в функции.
print_params(**values_dict) # Проверяем функцию со значениями словаря values_dict.

    # Р С П А К О В К А  +  О Т Д Е Л Ь Н Ы Е  П А Р А М Е Т Р Ы

value_list_2 = [54.32, 'Строка'] # Создаем список values_list_2
print_params(*value_list_2,42)  # Проверяем работу функции с вновь созданным списком.