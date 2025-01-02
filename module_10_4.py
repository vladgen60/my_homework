from threading import Thread
from random import  randint
import time
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name): # name имя гостя.
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guest):
        for table in self.tables:
            if table.guest is None:
                table.guest = guest
                return guest.name, table.number
        self.queue.put(guest)
        return  guest.name, None

    def discuss_guests(self):
        for table in self.tables:
            if table.guest is not None and not table.guest.is_alive():
                print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {table.number} свободен')
                table.guest = None
                if not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

# num_table = Table(1)
# num_guest = Guest('Vasya')

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

