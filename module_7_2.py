# Задача "Записать и запомнить":
# Импортируем необходимые библиотеки.
import io
from pprint import  pprint
def custom_write(file_name, strings): # Создаем функцию custom_write.
    n = 0 # Создаем переменную n и присваиваем ей начальное значение 0.
    elem = {}   # Создаем пустой словарь.
    for i in strings: # Итерируем список strings.
        file = open(file_name, 'w+', encoding='utf-8') # Открываем файл, с методом w+ и изменением кодировки..
        num_tell = (file.tell())
        n += 1
        file.write(f'{i}\n')
        file.close()
        elem.update({(n, num_tell):i}) # Метод update()  добавляет в словарь
                                    # одну или сразу несколько пар «ключ — значение».
    return elem

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)







