# Банковские операции
# Импортируем необходимые библиотеки.
import threading
from  random import randint
import time


class Bank: # Создаем класс Bank.
    def __init__(self): # Создаем конструктор класса.
        self.balance = 0  # Начальный баланс банка.
        self.lock = threading.Lock()  # Создаем объект Lock для блокировки потоков.

    def deposit(self): # Создаем метод depozit.
        counter = 100
        while counter > 0: # Цикл для 100 транзакций.
            my_plus = randint(50, 501)  # Генерируем случайное число от 50 до 500.
            self.lock.acquire()  # Блокируем доступ к ресурсу.
            self.balance += my_plus  # Увеличиваем баланс на .
            print(f"Пополнение: {my_plus}. Баланс: {self.balance}")  # Выводим информацию о пополнении.
            # Проверяем, если баланс больше или равен 500
            if self.balance >= 500:
                self.lock.release()  # Разблокируем замок, если необходимо.
            else:
                self.lock.release()  # Разблокируем замок, если не достигли порога.
            counter -= 1
            time.sleep(0.001)  # Ожидание в 0.001 секунды.

    def take(self): # Создаем метод для снятия средств.
       counter = 100
       while counter > 0:  # Цикл для 100 транзакций.
            my_minus = randint(50, 500)  # Генерируем случайное число от 50 до 500.
            print(f"Запрос на {my_minus}")  # Выводим запрос на снятие.

            self.lock.acquire()  # Блокируем доступ к ресурсу.
            if my_minus <= self.balance:  # Проверяем, достаточно ли средств на балансе.
                self.balance -= my_minus  # Уменьшаем баланс.
                print(f"Снятие: {my_minus}. Баланс: {self.balance}")  # Выводим информацию о снятии.
                self.lock.release()  # Разблокируем замок после успешного снятия.
            else:
                print("Запрос отклонён, недостаточно средств")  # Сообщаем об отказе в снятии.
                self.lock.release()  # Разблокируем замок, если недостаточно средств.
            counter -= 1
            time.sleep(0.001)  # Ожидание в 0.001 секунды


# Создаем объект класса Bank.
bk = Bank()

# Создаем потоки для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

# Выводим итоговый баланс после завершения всех операций.
print(f'Итоговый баланс: {bk.balance}')
