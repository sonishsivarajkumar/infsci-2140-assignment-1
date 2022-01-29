from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class WordNormalizer:
    def __init__(self):
        # self.stemmer = PorterStemmer()
        self.stemmer = SnowballStemmer(language='english')

    def lowercase(self, word: str):
        # Transform the word uppercase characters into lowercase.
        return word.lower()

    def stem(self, word):
        # stem using the NLTK stemmer of choice (I found Snowball to be fastest)
        return self.stemmer.stem(word)
