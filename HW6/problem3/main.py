#/usr/bin/python2.7
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import PorterStemmer

# [ 3-B ]
def filter_stopwords(string, stopwords):
    tweet = TweetTokenizer()
    return [x for x in tweet.tokenize(string) if x not in stopwords]

# [ 3-D ]
def do_stemming(string):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in string]
