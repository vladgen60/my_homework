# Потоковая запись в файлы

# Импортируем необходимые библиотеки.
from time import sleep
import time
import threading


def write_words(word_count, file_name):     # Создаем функцию write_words.
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write( f'Какое-то слово №  {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

time_start = time.time()    # Время начала выполнения записи с помощью функции.

# Вызываем 4 раза функцию wite_words.
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = time.time() # Время окончания выполнения записи с помощью функции.
time_res = time_stop - time_start # Общая длительность выполнения записи с помощью функции.
print(f'Время работы функций {time_res}') # Вывод длительности времени выполнения записи с помощью функций.

time2_start = time.time() # Время начала выполнения записи с помощью потоков.

# Создание и запуск четырех потоков с аргументами.
thread_first = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thread_second = threading.Thread(target=write_words, args= (30, 'example6.txt'))
thread_third = threading.Thread(target=write_words, args= (200, 'example7.txt'))
thread_fourh = threading.Thread(target=write_words, args= (100, 'example8.txt'))

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourh.start()

thread_first.join()
thread_second.join()
thread_third.join()
thread_fourh.join()

time2_stop = time.time()    # Время окончания работы потоков.
time2_res = time2_stop - time2_start    # Длительность времени работы потоков.
print(f'Время работы потоков {time2_res}') # Вывод длительности времени выполнения записи с помощью потоков.

print(f'Использование потоков быстрее функций на {time_res-time2_res} секунд') # Выводим разницу времени между длительностью 
                                                                                # функций и потоков.

