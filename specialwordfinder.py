from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """creates word finder that filters out spaces and comments 

    >>> word_finder = SpecialWordFinder('new_words.txt')
    4 words read
    
    >>> isinstance(word_finder.random(), str)
    True

    
    >>> word_finder.random().startswith('#')
    False

    >>> word_finder.random() == ''
    False
    """

    def __init__(self,path):
        super().__init__(path)
        self.word_list = self.generate_word_list(path)

    def generate_word_list(self, path):
        "Generates list that filters out empty and commented lines"
        f = open(path, 'r')
        lst = [line.rstrip('\n') for line in f if not line.startswith('#') and not line.rstrip('\n') == '']
        return lst