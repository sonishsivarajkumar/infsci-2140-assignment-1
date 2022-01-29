from nltk.tokenize import word_tokenize
import re
# Efficiency and memory cost should be paid with extra attention.
# Essential private methods or variables can be added.


class WordTokenizer:
    # per TA feedback, manually tokenize by keeping only letter expressions
    regex = re.compile('[a-zA-Z]+')

    def __init__(self, content: str):
        # Tokenize the input texts.

        # tracking our position inside the tokens so we can return None when we're done
        self.index = 0
        self.tokenized_content = WordTokenizer.regex.findall(content)

        return

    def nextWord(self):
        # Return the next word in the document.
        # Return null, if it is the end of the document.

        # increment the index
        self.index += 1

        # return None if we're out of bounds
        if self.index >= len(self.tokenized_content):
            return None

        # else return the token
        return self.tokenized_content[self.index]
