import util


def classify(s):
    tokens = util.tokenize(s)
    db = util.Database()
    c = db.getCursor()

    # Prior probabilities
    pos_words = []
    neg_words = []
    neu_words = []
    for c in c.execute("SELECT * FROM training_data"):
        if c[1] == 1:
            pos_words += eval(c[0])
        elif c[1] == -1:
            neg_words += eval(c[0])
        else:
            neu_words += eval(c[0])
    all_words = pos_words+neg_words+neu_words
    pos_prior = float(len(pos_words))/len(all_words)
    neg_prior = float(len(neg_words))/len(all_words)
    neu_prior = float(len(neu_words))/len(all_words)

    # For positive
    prob_prod = 1.0
    for token in tokens:
        prob_prod *= float((pos_words.count(token)+1))/(len(pos_words)+len(all_words))
    pos_prob = prob_prod * pos_prior
    print prob_prod

    # For negative
    prob_prod = 1.0
    for token in tokens:
        prob_prod *= float((neg_words.count(token)+1))/(len(neg_words)+len(all_words))
    neg_prob = prob_prod * neg_prior
    print prob_prod

    # For neutral
    prob_prod = 1.0
    for token in tokens:
        prob_prod *= float((neu_words.count(token)+1))/(len(neu_words)+len(all_words))
    neu_prob = prob_prod * neu_prior
    print prob_prod

    return pos_prob, neg_prob, neu_prob

# print classify(raw_input("Enter a sentence to classfiy: "))

