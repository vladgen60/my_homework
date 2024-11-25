import math # Импорт библиотеки math

class Figure(): # Создание класса Figure.
    side_count = 0 # Аттрибут класса.
    def __init__(self, color, *sides):   
        self.__color = color
        self.__sides = []
        self.filled = False
           
    def get_color(self): # Метод возвращает список цветов.
        return self.__color   
        
    def __is_valid_color(self, r, g, b): # Метод проверяет корректность цветов.
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))
   

    def set_color(self, r, g, b):    # Метод принимает параметры цветов.  
            if self.__is_valid_color(r, g, b):
                self.__color = [r, g, b]  

    def __is_valid_sides(self, *new_sides): # Метод  проверяет количество сторон и что все стороны - положительные целые числа.       
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)       

    def get_sides(self):      # Метод возвращает список сторон фигуры.
        return self.__sides  

    def set_sides(self, *new_sides): # Метод проверяет корректность новых сторон и устанавливает новые.
        if self.__is_valid_sides(*new_sides):  
            self.__sides = list(new_sides)  

    def __len__(self):  # Метод возвращает периметр фигуры.
        return sum(self.__sides)  
             
    

class Circle(Figure): # Создаем класс Circle наследующий аттрибуты и методы класса Figure.
    sides_count = 1 # У окружности сторона одна.
    def __init__(self, color, long_circle):
        super().__init__(color)
        self.__radius = long_circle / (2 * math.pi)  # Рассчитываем радиус по длине окружности.
        self.set_sides(long_circle)  # Устанавливаем длину окружности как сторону.

    def get_square(self): # Метод возвращает площадь круга.
        return math.pi * (self.__radius ** 2)    

class Triangle(Figure): # Создаем класс Triangle наследующий аттрибуты и методы класса Figure.
    sides_count = 3  # У треугольника три стороны.

    def __init__(self, color, a, b, c): # 
        super().__init__(color, a, b, c)  

    def get_square(self): # Метод возвращает площадь треугольника.        
        a, b, c = self.get_sides()  
        s = (a + b + c) / 2  
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Площадь.
    

class Cube(Figure): # Создаем класс Cube наследующий аттрибуты и методы класса Figure.
    sides_count = 12  # У куба двенадцать рёбер

    def __init__(self, color, cub_length):
        super().__init__(color)  

        self.set_sides(*[cub_length] * self.sides_count)
        
    def get_volume(self): # Метод возвращает объём куба.        
        cub_length = self.get_sides()[0]  
        return cub_length ** 3 

    # П Р И М Е Р Ы

circle1 = Circle((200, 200, 100), 10)  # Создаем объект круга с цветом и длиной окружности
cube1 = Cube((222, 35, 130), 6)  # Создаем объект куба с цветом и длиной ребра

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменение цвета круга
print(circle1.get_color())  # Выводим текущий цвет круга: [55,66,77]
cube1.set_color(300, 70, 15)  # Попытка изменить цвет куба на некорректный
print(cube1.get_color())  # Выводим текущий цвет куба: [222,35,130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12)  # Попытка изменить стороны куба на некорректные
print(cube1.get_sides())  # Выводим текущие стороны куба: [6]*12
circle1.set_sides(15)  # Изменение стороны круга на новую длину окружности
print(circle1.get_sides())  # Выводим текущие стороны круга: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Выводим длину окружности: ~15.71

# Проверка объёма (куба):
print(cube1.get_volume())  # Выводим объём куба: ~216