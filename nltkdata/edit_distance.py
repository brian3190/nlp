# Edit Distance: The number of characters that can be inserted, substituted, deleted
# in order to make two strings equal
import nltk
from nltk.metrics import *
print(edit_distance("relate", "relation"))
print(edit_distance("suggestion", "calculation"))

# SmithWaterman Distance
# Binary Distance : 0 if similar, 1 if not similar
# Masi Distance : based on partial agrreement when multiple labels are present
