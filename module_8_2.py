#  "План перехват":
def personal_sum(numbers): # Создаем функцию personal_sum(numbers)
    result = 0
    incorrect_data = 0
    for i in numbers: # Итерируем нашу коллекцию.
        try:
            result += i # Код, где предположительно может появиться ошибка.
        except TypeError: # Отлавливаем предполагаемую ошибку.
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы: {i}') # Выводим на экран тип оошибки.
    return result, incorrect_data # Функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.

def calculate_average(numbers): # Создаем функцию принимающую коллекцию numbers и возвращющую: среднее арифметическое всех чисел.
    if isinstance(numbers, (int, float)): # Проверяем коллекцию на корректность данных.
        print('В numbers записан некорректный тип данных')
        return None
    else:
        try:                            # Пишем код в котором может появиться предполагаемая ошибка.
            x = personal_sum(numbers)
            if x[1] == len(numbers):    # Если делитель равен нулю.
                return 0
            else:
                return x[0] / (len(numbers) - x[1])
        except ZeroDivisionError:
            return 0
    



    # П Р И М Е Р Ы 

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать