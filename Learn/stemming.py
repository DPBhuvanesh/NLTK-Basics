from nltk.stem import PorterStemmer #portstemmer used for stemming

p=PorterStemmer()  #assign porterstemmer for p

text=['python','pythoner','pythoning','pythoner']

for i in text:
    print(p.stem(i))

#Use PorterStemmer , don't use porterstemmer 
