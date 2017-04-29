import nltk
corpus = nltk.corpus.brown.tagged_sents(categories='adventure')[:700]
print(len(corpus))
from nltk.util import unique_list
tag_set = unique_list(tag for sent in corpus for (word,tag) in sent)
print(len(tag_set))
symbols = unique_list(word for sent in corpus for (word,tag) in sent)
print(len(symbols))
trainer = nltk.tag.HiddenMarkovModelTrainer(tag_set, symbols)
train_corpus = []
test_corpus = []
for i in range(len(corpus)):
    if i % 10:
        train_corpus += [corpus[i]]
    else:
        test_corpus += [corpus[i]]

print(len(train_corpus))
print(len(test_corpus))

def train_and_test(est):
    hmm = trainer.train_supervised(train_corpus, estimator=est)
    print('%.2f%%' % (100 * hmm.evaluate(test_corpus)))
