#  "Найдёт везде"

class WordsFinder: # Создаем класс WordsFinder.
    def __init__(self, *file_name): # Создаем конструктор класса.
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self): # Создаем метод, который возвращает словарь.
        all_words = {}
        words = []
        str_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file: # Перебираем все в файле.
                    line = line.lower() # Переводим все в нижний регистр.
                    for p in str_punctuation: # Убираем пунтуацию.
                        if p in line:
                            line = line.replace(p, ' ') # Заменям все знаки пунтуации на ничего
                    split_line = line.split()
                    words.append(split_line) 
                    sorted_list = [x for y in words for x in y]
        all_words[file_name] = sorted_list # Создаем словарь где: ключ - имя файла, значение содержимое.
        return all_words

    def find(self, word): # Создаем метод, где word искомое слово. Возвращает словарь, где ключ - название файла,
                          # значение - позиция первого такого слова в списке слов этого файла.
        dict_words = self.get_all_words()
        list_words = []
        list_index = []
        for name, words in dict_words.items():            
            for w in words:
                if word.lower() in w:
                    index = words.index(w)                   
                    list_words.append(name)                                        
                    list_index.append(index + 1)
                    list_dict = dict(zip(list_words, list_index))                  
        return list_dict

    def count(self, word):  # Создаем метод, где word - искомое слово. Возвращает словарь, 
                            # где ключ - название файла, значение - количество слова word в списке слов этого файла.
        dict_1 = self.get_all_words()
        list_name = []
        list_count = []
        count = 0
        for name, words in dict_1.items():
            for w in words:
                if word.lower() in w:
                    count += 1
        list_name.append(name)
        list_count.append(count)
        dict_list = dict(zip(list_name, list_count))
        return dict_list

# Р Е З У Л Ь Т А Т Ы

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))