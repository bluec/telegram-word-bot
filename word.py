import re


class Word:
    def __init__(self, word=''):
        self.word = word
        self.length = self.get_length()
        self.letters = {}
        self.get_unique_letters()
        self.vowels_count = self.get_vowels_count()
        self.most_frequent_count = 0
        self.most_frequent_chars = []
        self.get_most_frequent_letters()

    def validate(self):
        if re.search('^[a-zA-Z]+$', self.word):
            return True
        else:
            return False

    def get_length(self):
        return len(self.word)

    def get_unique_letters(self):
        for character in self.word.lower():
            if character in self.letters:
                self.letters[character] = self.letters[character] + 1
            else:
                self.letters[character] = 1

    def get_vowels_count(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_count = 0
        for character in self.word.lower():
            if character in vowels:
                vowels_count += 1
        return vowels_count

    def get_most_frequent_letters(self):
        for key in self.letters:
            if self.letters[key] > self.most_frequent_count:
                self.most_frequent_count = self.letters[key]
                self.most_frequent_chars = [key]
            elif self.letters[key] == self.most_frequent_count:
                self.most_frequent_chars.append(key)

