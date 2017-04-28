import nltk
from replacers import WordReplacer
replacer = WordReplacer({'congrats':'congratulations'})
replacer2 = WordReplacer({'maths':'mathematics'})
syn = replacer.replace('congrats')
print syn
syn2 = replacer2.replace('maths')
print syn2
