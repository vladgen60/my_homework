# Задача "Ошибка эволюции":

import random # Импортируем библиотеку для вызова случайных чисел.

# Создаем класс Animal.
class Animal:
    live = True # Создаем атрибуты класса.
    sound = None
    _DEGREE_OF_DANGER = 0

    # Создаем методы класса.
    def __init__(self, speed):
        self._cords = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz): # Метод изменения координат.
        x1 = self._cords[0] + dx * self.speed
        y1 = self._cords[1] + dy * self.speed
        z1 = self._cords[2] + dz * self.speed
        if z1 < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [x1, y1, z1]

    def get_cords(self): # Метода вывода координат в нужном формате.
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):   # Вывод сообщения в зависимости от степени опасности.
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peacful :)")
        else:
            print("Be careful, i'm atacking you 0_0")

    def speak(self): # Вывод строки со звуком sound.
        print(self.sound)

# Создаем класс описывающий птиц, наследующий класс Animal.
class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        num_eggs = random.randint(1, 4)
        print(f'Here are(is) {num_eggs} eggs for you')

# Создаем класс описывающий плавающего животного, наследующий класс Animal.
class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z_change = abs(dz) * self.speed / 2
        new_z = self._cords[2] - z_change
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z

# Создаем класс PoisonousAnimal описывающий ядовитых животных, наследующий класс Animal.
class PoisonousAnimal (Animal):
    def __init__(self,speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

# Создаем класс Duckbill, описывающий утконоса, наследующий классы Bird, AquaticAnimal, PoisonousAnimal.
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = ' Click-click-click'

        # Пример работы программы:
#print(Animal.mro())
#print(Bird.mro())
#print(Duckbill.mro())

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()


