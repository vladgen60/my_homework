# Некорректность

class Car:  # Создаем класс Car.
    def __init__(self, model, vin, numbers): # Создаем конструктор класса.
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):   # Создаем метод принимающий vin_number и проверяющий его на корректность.
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not (1000000 <= vin_number <= 9999999): #  Если vin номер не в диапазоне.
            raise IncorrectVinNumber("Неверный диапазон для vin номера")    # Выбрасывает исключение.
        else:
            return True # Возвращает True, если корректный.

    def __is_valid_numbers(self, numbers): # Создаем метод принимающий numbers.
        if not isinstance(numbers, str):    # Проверяет numbers на корректность.
            raise IncorrectCarNumbers("Некорректный тип данных для номеров") # Выбрасывает если numbers не строка.
        if len(numbers) != 6:   # Проверяет numbers на длину.
            raise IncorrectCarNumbers("Неверная длина номера")  # Выбрасывает если длина не равна 6.
        else:
            return True # Возвращает True, если корректный.

class IncorrectVinNumber(Exception):    # Создаем класс исключений, выводит сообщиение при выбрасывании исключений.
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):   # Создаем класс исключений, выводит сообщиение при выбрасывании исключений.
    def __init__(self, message):
        self.message = message

    #    Р Е З У Л Ь Т А Т Ы

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


