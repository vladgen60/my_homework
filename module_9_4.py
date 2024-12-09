# Функциональное разнообразие

# Lambda-функция:

# Даны две строки.
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda  x, y:  x == y, first,  second )) # Составляем lambda-функцию.
print(result)

# Замыкание

def get_advanced_writer(file_name): # Создаем функцию принимающую название файла для записи.
    def write_everything(*data_set): # Создаем еще одну функцию принимающую неограниченное количество данных любого типа.
        with open(file_name, 'a', encoding='utf-8') as file: # Открываем файл в режиме append.
            for data in data_set:
                file.write(str(data) + '\n') # Добавляем данные в файл.
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice # Импорт библиотеки.

class MysticBall: # Создаем класс MysticBall, объекты которого обладают атрибутом words.
    def __init__(self, *words): # Создаем конструктор класса.
        self.words = words

    def __call__(self): # Определяем метод __call__ который будет случайным образом выбирать слово из words и возвращать его.
        return choice(self.words)

# Вывод результата
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


