#!/usr/bin/python2
from nltk.tokenize import TweetTokenizer
from nltk import PorterStemmer
import re


vocab={"UNKNOWN":0}
category_count={
    "spam":0,
    "ham":0
}
category_count_word={
    "spam":{"UNKNOWN":0},
    "ham":{"UNKNOWN":0}
}

# [ 3-A ]
def replace_regexp(string):
    #URLs
    string=re.sub(r"(\w+://|[Ww]{3}\.)([A-Za-z0-9_-]+\.)+[A-Za-z]{2,5}(/[A-Za-z0-9_-]+)*/?", "<URL>", string)
    #Phone
    string=re.sub(r"\+?[0-9][0-9 -]{3,}[0-9]\+?", "<PHONE>", string)
    #Prices TODO: add pounds and euro
    string=re.sub(r"[$][0-9]+([,\.][0-9]+)?", "<PRICE>", string)

    return string

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
    #If we have already seen this word
    if(string in vocab.keys()):
        vocab[string]+=1
        category_count_word[label][string]=category_count_word[label].get(string, 0)+1
    #New word, doesn't exceed the max size of the voc
    elif(len(vocab)<=VOCMAX):
        vocab[string]=1
        category_count_word[label][string]=1
    #We exceed the max size of the voc
    else:
        vocab["UNKNOWN"]+=1
        category_count_word[label]["UNKNOWN"]+=1

def train(labels, strings):
    for (label, string) in zip(labels, strings):
        category_count[label]+=1
        for word in string:
            add_voc(label, word)
    return 0

def complete_train():
    #Loading stopWords
    stopwords=[]
    print("Loading stopwords...")
    with open("stopwords.txt") as stopwords_file:
        for word in stopwords_file.readline().split(','):
            stopwords.append(word[1:-1])
    print("Stopwords loaded")



    print("Loading and preprocess training cases...")
    labels=[]
    strings=[]
    with open("train") as train_file:
        for line in train_file:
            [label, string]=line.split('|', 1)

            raw_string=replace_regexp(string)
            list_word=filter_stopwords(raw_string, stopwords)
            stemmed_word=do_stemming(list_word)

            labels.append(label)
            strings.append(stemmed_word)
    print("Training cases loaded and preprocessed")

    print("Training knowledge base...")
    train(labels, strings)
    print("Knowledge base trained")

complete_train()
