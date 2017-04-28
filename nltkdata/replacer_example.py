import nltk
from replacers import RegexpReplacer
replacer = RegexpReplacer()
text1 = replacer.replace("Don't hesitate to ask questions")
print text1
text2 = replacer.replace("She must've gone to the market but she didn't go")
print text2
