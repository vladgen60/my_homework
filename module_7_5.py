# Файлы в операционной системе"
# Импорт модуля OS и time
import os
import time

print()

directory = "."

# root -  строка, содержащая путь к текущему подкаталогу.
# dirs -  список строк, содержащий имена подкаталогов, находящихся в текущем подкаталоге.
# files - список строк, содержащий имена файлов, находящихся в текущем подкаталоге.

# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
for root, dirs, files in os.walk(directory):
    for file in files:        
        file_path = os.path.join(root, file)        
        file_time = os.path.getmtime(file_path)      
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))       
        file_size = os.path.getsize(file_path)       
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
