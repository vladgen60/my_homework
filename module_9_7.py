#  Декораторы.

def is_prime(func): # Создаем функцию декоратор, которая определяет является ли число простым или нет.
    def wrapper(*args): # Внутри функции is_prime создаем функцию wrapper.
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                return f'Составное\n{result}'
        else:
            return f'Простое\n{result}'
    return wrapper

@ is_prime  # Оборачиваем функцию sum_free.
def sum_three(*args): # Создаем функцию, которая складывает 3 числа (sum_three).
    result = sum(args)
    return result

    # Р Е З У Л Ь Т А Т

result = sum_three(2,3,6)
print(result)