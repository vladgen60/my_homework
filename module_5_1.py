# Задача "Developer - не только разработчик":

class House:    # Создаем класс объекта.
    def __init__(self, name, number_of_floors): # Создаем специальный метод init, который будет вызываться всегда,
                                                # когда будем вызывать экземпляр класса.
        self.name = name                        
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):          # Создаем еще один метод.       
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(1,new_floor + 1):
                print(i)

# П Р И М Е Р       
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)