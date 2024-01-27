from nltk.stem import PorterStemmer #portstemmer used for stemming

p=PorterStemmer()  #assign porterstemmer for p

text=['simbu','simbooo','simbi','simbee']

for i in text:
    print(p.stem(i))
