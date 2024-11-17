    # Задача "Изменять нельзя получать":

class Vehicle: # Создаем класс Vehicle
    """
    Создан класс в котором имеется атрибут класса __COLOR_VARIANTS, атрибуты: изменяемый owner и неизменяемые: __mode,
    __engine_power и __color
    """
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # Создаем уникальный атрибут класса Vehicle.
    def __init__(self, owner, __mode, __engine_power, __color):
        # Создаем атрибуты объекта класса Vehicle.
        self.owner = owner
        self.mode = __mode
        self.engine_power = __engine_power
        self.color = __color

        # Создаем методы класса Vehicle.

    def get_mode(self):
        return f'Модель: {self.mode}'
    def get_horsepower(self):
        return f'Мощность двигателя {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(f'{self.get_mode()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

    # Создаем класс Sedan.
class Sedan(Vehicle):
    """
    Создаем класс Sedan, который имеет атрибут класса __PASSENGERS_LIMIT и так же наследует атрибуты и методы
    класса Vehicle.
    """
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II',500 , 'blue')
# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось
vehicle1.print_info()




        