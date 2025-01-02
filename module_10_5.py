# Импортируем необходимые библиотеки.
from datetime import datetime
import multiprocessing


def read_info(name): # Создаем функцию read_info.
    all_data = []
    with open(name, encoding='utf-8') as file: # Открываем файл, по умолчанию в режиме чтения.
        while True: # Запускаем цикл до первой пустой строчки.
            line = file.readline()
            if line != '':
                all_data.append(line)
            else:
                break


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start_1 = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_1 = datetime.now()
    print(f'{end_1 - start_1} (линейный)')
    with multiprocessing.Pool(processes=8) as pool:
        start_2 = datetime.now()
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(f'{end_2 - start_2} (многопроцессный)')