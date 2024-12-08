# Необходимо создать 2 генераторных сборки

#   Дано 2 списка:
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = list((len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))) # В переменную first_result
# запиcываем генераторную сборку, которая высчитывает разницу длин строк из списков, если их длины не равны.

second_result = list((len(first[x]) == len(second[x])) for x in range(len(first))) # В переменную second_result
# запиcваем генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых позициях из списков.

# Р Е З У Л Ь Т А Т Ы

print(first_result)
print(second_result)
