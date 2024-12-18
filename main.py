import string

class WordsFinder:
    def __init__(self, *files_name):
        self.file_names = files_name
    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, 'r', encoding='utf-8') as file:
                file.seek(0)
                str = file.read()
                punctuation_chars = string.punctuation
                for punctuation in punctuation_chars:
                    str = str.replace(punctuation, ' ')
                    words = str.split()
                    all_words[filename] = words
        return all_words
    def find(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            if word in words:
                try:
                    index = words.index(word) + 1
                except ValueError:
                    index = None
                results[filename] = index
        return results
    def count(self, word):
        all_words = self.get_all_words()
        results = {}
        for filename, words in all_words.items():
            cnt = words.count(word)
            results[filename] = cnt
        return results
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))