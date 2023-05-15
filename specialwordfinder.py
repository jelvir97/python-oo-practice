from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """creates word finder that filters out spaces and comments 
    """

    def __init__(self,path):
        super().__init__(path)
        self.word_list = self.generate_word_list(path)

    def generate_word_list(self, path):
        f = open(path, 'r')
        lst = [line.rstrip('\n') for line in f if not line.startswith('#') and not line.rstrip('\n') == '']
        return lst