# Automated translation, before running type: pip install TextBlob
from textblob import TextBlob


print ("Enter sentence you like to translate:")

#input = raw_input() # for Python 2.7
input = input() # for Python 3

#t = 'Dieser Satz ist deutlich schwieriger zu ubersetzen, aber es scheint dennoch machbar.'


text = TextBlob(input)
text.translate()
print (text.translate().string)
