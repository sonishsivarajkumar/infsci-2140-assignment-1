import Classes.Path as Path

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class StopWordRemover:

    def __init__(self):
        # Load and store the stop words from the fileinputstream with appropriate data structure.
        # NT: address of stopword.txt is Path.StopwordDir.
        with open(Path.StopwordDir, 'r') as f:
            self.stop_words = [word.strip() for word in f.readlines()]

    def isStopword(self, word):
        # Return true if the input word is a stopword, or false if not.
        return word in self.stop_words
