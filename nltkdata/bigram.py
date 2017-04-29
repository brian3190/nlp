import nltk
from nltk.corpus import webtext
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
# Stopwords
set = set(stopwords.words('english'))
stops_filter = lambda w: len(w) < 3 or w in set
tokens=[t.lower() for t in webtext.words('grail.txt')]
words=BigramCollocationFinder.from_words(tokens)
# Apply stopwords
words.apply_word_filter(stops_filter)
y = words.nbest(BigramAssocMeasures.likelihood_ratio, 20)
print y
