    # Списковые, словарные сборки

#   Даны два списка, состоящие из строк.

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

#   В переменную first_result записываем список созданный при помощи сборки состоящий из длин строк списка
#   first_strings, при условии, что длина строк не менее 5 символов.
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

# В переменную second_result записываем список созданный при помощи сборки состоящий
# из пар слов(кортежей) одинаковой длины.
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print (second_result)

#  В переменную third_result записываем словарь созданный при помощи сборки,
#  где парой ключ-значение будет строка-длина строки.

    # В Ы В О Д  Р Е З У Л Ь Т А Т О В

third_result = first_strings + second_strings
third_result = {x: len(x) for x in third_result if len(x) % 2 == 0}
print(third_result)