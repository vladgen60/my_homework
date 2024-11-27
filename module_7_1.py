from pprint import pprint # Импорт библиотеки pprint.

class Product:  # Создание класса Product.
    def __init__(self, name, weight, category): # Создание конструктора класса.
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):  # Метод вывода строки.
        return f'{self.name}, {self.weight}, {self.category}'

class Shop: # Создание класса Shop.
    def __init__(self): # Создание конструктора класса.
        self.__file_name = 'products.txt'

    def get_products(self): # Метод считывающий информацию из файла и возращающий информацию в виде строки.
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products): # Метод добавляющий в файл название продукта, если его нет в файле.
        for i in products:
            if (i.name in self.get_products()):
                print(f'Продукт {i.name} уже есть в магазине') # Если есть название продукта в файле, то выводит сообщение, что такой уже есть.
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()


    #   П Р И М Е Р Ы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())