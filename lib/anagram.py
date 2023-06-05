class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        new_list = []
        for letter in list:
            if sorted(letter.lower()) == sorted(self.word.lower()):
                new_list.append(letter)
            else:
                return new_list