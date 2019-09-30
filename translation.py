# Automated translation, before running type: pip install TextBlob
from textblob import TextBlob
t = 'Dieser Satz ist deutlich schwieriger zu ubersetzen, aber es scheint dennoch machbar.'
text = TextBlob(t)
text.translate()
print (text.translate().string)
