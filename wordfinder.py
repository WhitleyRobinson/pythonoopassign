"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from the dictionary.
    
    >>> wf = WordFind("simple.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """Supposed to read dictionary and reports on # of items read."""
        
        dict_file = open(path)
        
        self.words = self.parse(dict_file)
        
        print(f"{len(self.words)} words read")
        
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return a random word."""
        
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """wordfinder that leaves out blank lines and comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read
    
    >>> swf.random() in ["pear", "Carrot", "kale"]
    True
    
    >>> swf.random() in ["pear", "Carrot", "kale"]
    True
    
    >>> swf.random() in ["pear", "Carrot", "kale"]
    True
    """
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blacks/comments."""
        
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]