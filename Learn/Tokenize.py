from nltk.tokenize import word_tokenize, sent_tokenize 
 #using nltk tokenzie and importing word and sentence tokenize.
text = "Hi this is me. welcome ! I am happy today. How are you?"
#example text 
print(word_tokenize(text)) #printing tokenized words

for i in sent_tokenize(text): #another method for printing to seprate sentences and words in new line
    print(i)