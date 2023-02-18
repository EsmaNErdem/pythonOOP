import random

class WordFinder:
    """ Finding random words from a file
    >>> dictionary = WordFinder("words.txt")
    Dictionary has 235887 words

    >>> dictionary.random() in dictionary.words
    True

    >>> 

    """


    def __init__(self, file):
        "Open dictionary and return # of words"
        open_file = open(file)
        self.words = self.get_words(open_file)
        print(f"Dictionary has {len(self.words)} words")
        
    def get_words(self, open_file):
        """Read the dictionary file I could do
            for line in open_file:
                line.strip()
            [line.stript() for line in open_file]
        """
        return open_file.read().split('\n')
        # do I need to close this open file everytime? 

    def random(self):
        "Returns a random word"
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Finding special words

    >>> complex_dictionary = SpecialWordFinder('complex.txt')
    Dictionary has 4 words

    >>> complex_dictionary.random() in complex_dictionary.words
    True
    """
    def get_words(self, open_file):
        return [word for word in open_file.read().split('\n') if not word.startswith('#') and word]

        