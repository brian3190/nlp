import nltk
corpus = nltk.corpus.brown.tagged_sents(categories='adventure')[:700]
print(len(corpus))
from nltk.util import unique_list
tag_set = unique_list(tag for sent in corpus for (word,tag) in sent)
