# За честь и отвагу!

# Импортируем необходимые библиотеки.
import threading
import time  

class Knight(threading.Thread): # Создаем класс наследованный от Thread.
    def __init__(self, name, power):    # Создаем конструктор класса.
        super().__init__()  
        self.name = name
        self.power = power
        self.enemy = 100
        self.days = 0

    def run(self):  
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            self.days += 1
            self.enemy -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {self.days} день(дня), осталось {self.enemy} воинов.')
        print(f'{self.name} одержал победу спустя {self.days} дней!')

#       Р Е З У Л Ь Т А Т Ы
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')



