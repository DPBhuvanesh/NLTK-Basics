from nltk.corpus import stopwords
#using nltk corpus to import stop_words
from nltk.tokenize import word_tokenize
#using word tokenize
stop_words=set(stopwords.words("english"))
#print(stop_words) use to print stop words of english

text =" practice makes perfect. Try and try until you succeed. Stay Hard"

token=word_tokenize(text)

filter_words=[w for w in token if w not in stop_words]

print(token)
#for i in token:
   # print(i) another way to print but we need to see difference so not needed
    
print(filter_words)

