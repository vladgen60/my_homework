class House:  # Создаем класс объекта.
    def __init__(self, name, number_of_floors):  # Создаем специальный метод init, который будет вызываться всегда,
        # когда будем вызывать экземпляр класса.
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):  # Создаем еще один метод.
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):  # Создаем метод возвращающий количество этажей.
       return self.number_of_floors

    def __str__(self):  # Создаем метод возвращающий название ЖК и количество этажей каждого.
        return 'Название: {}, количество этажей: {}'.format(self.name, self.number_of_floors)
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
       return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        self.number_of_floors += value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self

# Создаем два экземпляра класса h1 и h2.

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# П Р И М Е Р Ы
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__