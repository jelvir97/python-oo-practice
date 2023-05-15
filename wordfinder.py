"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    -Instatiates class with path to file.
    - creates list attribute from words in file
    """

    def __init__(self, path):
        self.word_list = self.generate_word_list(path)
        print(self.words_read())

    

    def generate_word_list(self, path):
        f = open(path, 'r')
        lst = []
        for line in f:

            lst.append(line.rstrip('\n'))
        f.close()
        return lst
    
    def random(self):
        return choice(self.word_list)
    
    def words_read(self):
        return f'{len(self.word_list)} words read'
