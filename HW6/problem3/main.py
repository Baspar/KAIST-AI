#/usr/bin/python2.7
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import PorterStemmer


vocab={"UNKNOWN":0}
category_count={
    "spam":0,
    "ham":0
}
category_count_word={
    "spam":{"UNKNOWN":0},
    "ham":{"UNKNOWN":0}
}

# [ 3-B ]
def filter_stopwords(string, stopwords):
    tweet = TweetTokenizer()
    return [x for x in tweet.tokenize(string) if x not in stopwords]

# [ 3-C ]
VOCMAX=10000



# [ 3-D ]
def do_stemming(string):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in string]

# [ 3-E ]
def add_voc(label, string):
    if(string in vocab.keys): #If we have already seen this word
        vocab[string]+=1
        if(string in category_count_word[label]): #If we have seen it in this category
            category_count_word[label][string]+=1
        else:#First time we see it uin thi category
            category_count_word[label][string]=1
    elif(vocab.size<=VOCMAX):#New word, doesn't exceed the max size of the voc
        vocab[string]=1
        category_count_word[label][string]=1
    else:#We exceed the max size of the voc
        vocab["UNKNOWN"]+=1
        category_count_word[label]["UNKNOWN"]+=1

def train(labels, strings):
    for label, string in labels, strings:
        category_count[label]+=1
        for word in string.split(' '):
            add_voc(label, word)
    return 0
