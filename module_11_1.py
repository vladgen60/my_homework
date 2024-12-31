# Обработка изображения
from PIL import Image
img = Image.open(r'C:\projects\learn1\my_picth.jpg')
#img.show(img)
# print(img.format)
# print(img.size)
# print(img.mode)

# Изменение размеров изображения.
cord = (400, 100, 740, 550) # лево, верх, право, низ
new_picture = img.crop(cord)
new_picture.show()

def change_color(image_paths): # Функция изменения цвета изображения
    image = Image.open(image_paths)
    image = image.convert('L')
    return image.save(image_paths)

change_color(r'C:\projects\learn1\my_picth.jpg')

# Работа с массивами с помощью библиотеки numpy
import numpy as np
a = np.arange(15).reshape(3, 5) # Создаем 2-х мерный массив.
b = np.arange(15,30).reshape(3,5)
print('Выводим в консоль массив a: \n{}'.format(a))    # Выводим массив a в консоль.
print('')
print('Выводим в консоль массив b \n{}'.format(b))   # Выводим массив b  в консоль.
print('')
print('Выводим в консоль сложение массивов a + b: \n{}'.format(a + b)) # Складываем массивы а и b и выводим в консоль.
print('')
print('Выводим в консоль умножение массивов a * b: \n{}'.format(a * b)) # Перемножаем массивы а и b и выводим в консоль.
print('')
print('Выводим в консоль вычитание массивов b - a: \n{}'.format(b - a)) # Вычитаем массивы а и b и выводим в консоль.
print('')
print('Выводим в консоль деление массивов a / b: \n{}'.format(a / b)) # Делим массивы а и b и выводим в консоль.


import matplotlib.pyplot as plt
fig, ax = plt.subplots()             # Создание осей координат на плоскости.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Создание в этих осях графика.
plt.show()  # Вывод осей с графиком в консоль.

