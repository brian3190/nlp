import nltk
from nltk.util import ngrams
sent = "Hello, please read the book thoroughly. If you have any queries, then don't hesitate to ask. There is no shortcut to success."
n = 5
fivegrams = ngrams(sent.split(), n)
for grams in fivegrams:
    print(grams)

'''
import os

corpus = []
path = '.'
for i in os.walk(path).next()[2]:
    if i.endswith('.txt'):
        f = open(os.path.join(path,i))
        corpus.append(f.read())
frequencies = Counter([])
for text in corpus:
    token = nltk.word_tokenize(text)
    bigrams = ngrams(token, 2)
    frequencies += Counter(bigrams)
'''
