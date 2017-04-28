# Plot of rank versus frequency of words in a document
# Zipf's law: frequency of a token in a text is directly proportional to rank or position
# in the sorted list.
import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
fd = FreqDist()
for text in gutenberg.fileids():
    for word in gutenberg.words(text):
        fd[word.lower()] += 1
ranks = []
freqs = []
for rank, word in enumerate(fd):
    ranks.append(rank+1)
    freqs.append(fd[word])

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()
