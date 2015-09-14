from nltk.tokenize import word_tokenize
import string
import sqlite3


class Database(object):

    def __init__(self):
        self.conn = sqlite3.connect("data.db")
        self.c = self.conn.cursor()

        # if this is the first time
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS training_data (message, label)"
            )
        self.conn.commit()

    def getCursor(self):
        return self.c

    def close(self):
        self.conn.commit()
        self.conn.close()


def tokenize(s):
    """
    Tokenizes and negates sentences
    E.g. "This isn't a cool movie, but it's worth it"
    returns the tokenized form:
    "This isn't NOT_a NOT_cool NOT_movie, but it's worth it"
    """
    tokens = word_tokenize(s.lower())
    punc_list = [i for i in string.punctuation]
    in_negative = False
    new_tokens = []
    for token in tokens:
        if token == "n't" or token == 'not':
            in_negative = True
        elif token in punc_list:
            in_negative = False
        if in_negative and token is not "not":
            token = "NOT_"+token
        new_tokens.append(token)

    return new_tokens

