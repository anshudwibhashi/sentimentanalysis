import util


def train():
    """
    Accept text messages from the user and whether or not it's a positive
    or negative message to train a classifier.
    """

    db = util.Database()
    c = db.getCursor()
    while True:
        s = raw_input("Enter sentence or \".\" to stop training: ")
        if s == ".":
            break

        tokens = repr(util.tokenize(s))
        l = raw_input(
            "Is this a positive (1), neutral(0) or negative(-1) sentence: "
            )
        label = int(l)
        c.execute("INSERT INTO training_data VALUES (?,?)", (tokens, label))

    db.close()

# train()

# db = util.Database()
# for c in db.getCursor().execute("SELECT * FROM training_data"):
#     print c[0], c[1]

