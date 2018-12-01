from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'term_list.txt'),encoding='utf-8').read()

_text = text.split("\n")
file = open('term.txt','w',encoding='utf-8') 
for s in _text:
    words = s.split(",")
    for word in words:
        w = word.strip()
        file.write(w)
        file.write("\n")
file.close()