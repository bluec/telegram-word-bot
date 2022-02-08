import re


class Word:
    def __init__(self, word=''):
        self.word = word
        self.length = self.get_length()
        self.unique_letters = self.get_unique_letters()
        self.vowels_count = self.get_vowels_count()
        self.consonants_count = self.get_consonants_count()
        self.most_frequent_letters, self.most_frequent_letters_count = self.get_most_frequent_letters()

    def validate(self) -> bool:
        if re.search('^[a-zA-Z]+$', self.word):
            return True
        else:
            return False

    def get_length(self) -> int:
        return len(self.word)

    def get_unique_letters(self) -> dict:
        letters = {}
        for character in self.word.lower():
            if character in letters:
                letters[character] = letters[character] + 1
            else:
                letters[character] = 1
        return letters

    def get_vowels_count(self) -> int:
        return len(self.get_vowels())

    def get_consonants_count(self) -> int:
        return len(self.get_consonants())

    def get_vowels(self) -> str:
        vowel_chars = ['a', 'e', 'i', 'o', 'u']
        vowels = ''
        for character in self.word.lower():
            if character in vowel_chars:
                vowels += character
        return vowels

    def get_consonants(self) -> str:
        vowel_chars = ['a', 'e', 'i', 'o', 'u']
        consonants = ''
        for character in self.word.lower():
            if character not in vowel_chars:
                consonants += character
        return consonants

    def get_most_frequent_letters(self) -> tuple:
        highest_count = 0
        unique_letters = self.get_unique_letters()
        most_frequent_letters = []
        for key in unique_letters:
            if unique_letters[key] > highest_count:
                highest_count = unique_letters[key]
                most_frequent_letters = [key]
            elif unique_letters[key] == highest_count:
                most_frequent_letters.append(key)
        return most_frequent_letters, highest_count
