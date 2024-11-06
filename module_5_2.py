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
    
    def __len__(self):                  # Создаем метод возвращающий количество этажей.
        return self.number_of_floors

    def __str__(self):                  # Создаем метод возвращающий название ЖК и количество этажей каждого.
        return 'Название: {}, количество этажей: {}'.format(self.name,self.number_of_floors)

# Создаем два экземпляра класса h1 и h2.

h1 = House('ЖК Эльбрус', 10) 
h2 = House('ЖК Акация', 20)

# П Р И М Е Р Ы

# __str__

print(h1)
print(h2)

# __len__

print(len(h1))
print(len(h2))