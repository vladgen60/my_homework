        # РЕШЕНИЕ ПРИ ПОМОЩИ ОПЕРАТОРА IN.

def single_root_words(root_word, *other_words): # Определяем функцию.
    same_words = []     # Создаем пустой список, куда будем добавлять нужные слова.
    
    for i in range(len(other_words)): # Перебираем номера элементов списка other_words.

        # Составляем условие при котором слово входящее в 1-й параметр функции входит в состав слова
        # из списка второго параметра без учета регистра и также слова из списка второго параметра входят
        # в состав слова первого параметра функции, также без учета регистра. 
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():            
            same_words.append(other_words[i]) # Добавляем слово отвечающее условиям выше в список same_words.
    return (same_words) #   Возвращаем список в функцию.

    #   ПРИМЕРЫ 

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

        # РЕШЕНИЕ ПРИ ПОМОЩИ МЕТОДА COUNT.

def single_root_words(root_word, *other_words): # Определяем функцию.
    same_words = []   # Создаем пустой список, куда будем добавлять нужные слова.

    for i in range(len(other_words)):   # Перебираем номера элементов списка other_words.

           # Составляем условие при котором слово входящее в 1-й параметр функции входит в состав слова
        # из списка второго параметра без учета регистра и также слова из списка второго параметра входят
        # в состав слова первого параметра функции, также без учета регистра
        if (other_words[i].lower()).count(root_word.lower()) != 0 or (root_word.lower()).count(other_words[i].lower()) != 0:
            same_words.append(other_words[i])   # Добавляем слово отвечающее условиям выше в список same_words.
    return (same_words) #   Возвращаем список в функцию.

         #   ПРИМЕРЫ 

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)   