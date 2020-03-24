import nltk
paragraph= """ A paragraph (from the Ancient Greek παράγραφος paragraphos, 
                "to write beside" or "written beside") is a self-contained unit of a discourse 
                in writing dealing with a particular point or idea. 
                A paragraph consists of one or more sentences. Though not required by the syntax 
                of any language, paragraphs are usually an expected part of formal writing, 
                used to organize l . """

# clearing the texts 
import re # regular expressions
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]',' ',sentences[i])   # remove everything in the ith sentence except a-zA-Z 
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# CREATING THE BAG OF WORDS
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
x = cv.fit_transform(corpus).toarray()

print(x)