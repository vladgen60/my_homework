# Задача "Съедобное, несъедобное":

class Animal: # Создаем класс Animal.
    alive = True    # Создаем атрибуты класса.
    fed = False    
    def __init__(self, name): # Создаем метод
        self.name = name

class Plant: # Создаем класс Plant
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal): # Создаем класс Mammal наследующий атрибуты и методы класса Animal.
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Predactor(Animal): # Создаем класс Predactor наследующий атрибуты и методы класса Animal.
    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        
class Flower(Plant):    #  Создаем класс Flower наследующий атрибуты и методы класса Plant.
    pass                

class Fruit(Plant):     # # Создаем класс Fruit наследующий атрибуты и методы класса Plant.
    def __init__(self, name):
        self.name = name
        self.edible = True

# Создаем экземпляры классов.
a1 = Predactor('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Выводим на экран.

print(a1.name)
print(a2.name)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


    

    
