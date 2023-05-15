"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """
    -Instatiates class with path to file.
    -creates list attribute from words in file

    >>> word_finder = WordFinder('words.txt')
    235886 words read

    >>> isinstance(word_finder.random(), str)
    True
    """

    def __init__(self, path):
        self.word_list = self.generate_word_list(path)
        print(self.words_read())

    

    def generate_word_list(self, path):
        """ Generates list of words from file"""
        f = open(path, 'r')
        lst = []
        for line in f:

            lst.append(line.rstrip('\n'))
        f.close()
        return lst
    
    def random(self):
        "Returns a random word from word_list"
        return choice(self.word_list)
    
    def words_read(self):
        "returns str with # of words read"
        return f'{len(self.word_list)} words read'
