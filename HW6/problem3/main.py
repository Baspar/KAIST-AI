#/usr/bin/python2.7
from nltk.tokenize import TweetTokenizer

# [ 3-B ]
def filter_stopwords(string, stopwords):
    return [x for x in TweetTokenizer().tokenize(string) if x not in stopwords]
