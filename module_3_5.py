        # Р Е К У Р С И Я

def get_multiplied_digits(number):  # Объявляем функцию с параметром.
    str_number = str(number)    #   Преобразуем параметр int в str.
    first = int(str_number[0])  #   Преобразуем первый элемент строки в int.
    if len(str_number) == 1:    #   Создаем условие: если число из одной цифры, то возвращаем это число в функцию.
        return first
    else:                          #    Иначе.
        if len(str_number) - 1 > 0: # Создаем условие: если длина числа минус 1 больше 0,
            return first * get_multiplied_digits(int(str_number[1:]))   # то возвращаем в функцию вычисленное значение.

        # П Р И М Е Р

result = get_multiplied_digits(40203)
print(result)

