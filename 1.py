import os

class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

        # Создаем файл, используя переданное имя
        with open(self.file_names, 'w', encoding='utf-8') as f:
            f.write("It's a text for task найти везде Используйте его для самопроверки Успехов в решении задачи text text text")

    def get_all_words(self):
        print("Рабочая директория:", os.getcwd())
        all_words = {}
        for file_name in [self.file_names]:
            with open(file_name, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    line = line.lower()
                    for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ', '—']:
                        line = line.replace(punctuation, ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    # Возвращаем методы `find` и `count`:
    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                result[file_name] = words.index(word.lower())
            except ValueError:
                result[file_name] = -1  # Если слово не найдено
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower())
        return result

finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

