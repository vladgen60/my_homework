calls = 0   # Создаем глобальную переменную calls и присваиваем ей значение 0.

def count_calls():  # Создаем функцию.
    global calls    # Переменной calls, присваиваем свойство при котором она сохраняет изменения, не только в локальном
                    # пространстве, но и в глабальном.
    calls = calls + 1 # При каждом вызове функции cals, значение будет увеличиваться на 1.
    return calls    # Возвращаем новое значение в функцию.

def string_info(string):    # Создаем функцию string_info().
    global calls            # Переменной calls, присваиваем свойство при котором она сохраняет изменения,
                            # не только в локальном пространстве, но и в глабальном.
    count_calls()           # Вызываем функцию count_calls.
    tuple_1 = (len(string),string.upper(),string.lower()) # Создаем кортеж из длины строки, строки в верхнем регистре и
                                                          # строки в ниженем регистре.
    return(tuple_1)  # Возвращаем созданный кортеж в функцию.
def is_contains(string, list_to_search): # Создаем функцию is_contains().
    global calls    # Переменной calls, присваиваем свойство при котором она сохраняет изменения, не только в локальном
                    # пространстве, но и в глабальном
    count_calls()   # Вызываем функцию count_calls.
    for i in list_to_search:    # Перебираем все элементы списка list_to_search.
        if string.lower() == i.lower(): # Если элемент строка равна  элементу списка, без учета регистра.
            return(True)    # Возвращаем True.
        else:
            return(False)   # Возвращаем False.

        # Выводим созданные функции на экран.
        # ______________________________________

print(string_info('Большой привет!'))
print(is_contains('Привет', ['привет', 'добрый день','20','45']))
print(is_contains('Привет!', ['привет', 'добрый день','20','45']))
print(count_calls())