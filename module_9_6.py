
def all_variants(text): # Создаем  функцию-генератор all_variants(text)
    for i in range(len(text)): # Перебираем область равную длине строки.
        yield text[i]   # Возвращаем все символы строки по одному.
    yield text[0] + text[1] # Возвращаем первый и второй символы строки.
    yield text[1] + text[2] # Возвращаем второй и третий символы строки.
    yield text  # Возвращаем всю строку.


# П Р И М Е Р Ы

a = all_variants('abc')
for i in a:
    print(i)