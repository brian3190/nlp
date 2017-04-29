# Generating bigrams from a text
import nltk
from nltk.collocations import *
from nltk.corpus import webtext
text1 = "Hardwork is the key to success. Never give up!"
tokens = [t.lower() for t in webtext.words('grail.txt')]
word = nltk.wordpunct_tokenize(text1)
# change argument to tokens to analyze grail.txt
finder = BigramCollocationFinder.from_words(word)
# apply frequency filer ignoring all bigrams which occur less than 3 times in corpus
### finder.apply_freq_filter(3)
bigram_measures = nltk.collocations.BigramAssocMeasures()
### print finder.nbest(bigram_measures.pmi, 10)
value = finder.score_ngrams(bigram_measures.raw_freq)
y = sorted(bigram for bigram, score in value)
print y
