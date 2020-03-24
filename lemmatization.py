                ##LEMMATIZATION


import nltk                           #importing nlt
from nltk.stem import WordNetLemmatizer   # PorterStemmer is imported from nltk.stem
from nltk.corpus import stopwords     # stopwords has basic words such as 'the' , 'that' , 'there'
paragraph = """ A paragraph is a number of sentences grouped together and relating to one topic. Or, a group of related sentences that develop a single point. This definition shows that the paragraphs of compositions are not mere arbitrary divisions. The division of a chapter into paragraphs must be made according to the changes of ideas introduced. """
sentences = nltk.sent_tokenize(paragraph)  #tokenizing paragraph into sentences , this variable sentences is a LIST having sentences separated .
Lemmatizer = WordNetLemmatizer()             # creates a stemmer objebct of class PorterStemmer

# stemming



for i in range(len(sentences)):       #iterating through the list , each sentence separated . 
    words=nltk.word_tokenize(sentences[i])   #tokenizing words in each sentence 
    words=[Lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]  #if word is in stopwords list don't fo anything , otherwise do stemming
    sentences[i]=' '.join(words)    #join the words to make each sentence stemmed .
print(sentences)
    
