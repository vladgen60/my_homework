# "Range - это просто"

class StepValueError(ValueError): # Создаем класс исключения StepValueError, который наследуется от ValueError.
    pass

class Iterator: # Создаем класс Iterator.

    def __init__(self, start, stop, step=1): # Создаем конструктор класса с атрибутами.
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self): # Создаем метод, сбрасывающий значение pointer на start.
        self.pointer = self.start
        return self

    def __next__(self): # Создаем  метод, увеличивающий атрибут pointer на step.
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        result = self.pointer
        self.pointer += self.step
        return result

#   Р Е З У Л Ь Т А Т Ы   

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1: 
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')



# iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


# for i in iter2:
#     print(i, end=' ')
# print()

for i in iter3:
    print(i, end=' ')
print() 

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()



    