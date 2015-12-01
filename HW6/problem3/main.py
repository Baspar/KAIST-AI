#!/usr/bin/python2
from nltk.tokenize import TweetTokenizer
from nltk import PorterStemmer
import re


#Sorted voc+cardinality
vocab={"UNKNOWN":0}
category_count={
    "spam":0,
    "ham":0
}
category_count_word={
    "spam":{"UNKNOWN":0},
    "ham":{"UNKNOWN":0}
}

#List of stopwords
stopwords=[]

#Total probabilities
p_ham=1.
p_spam=1.

#Test sorting
test_sorting={
    "ham":{
        True:0,
        False:0
    },
    "spam":{
        True:0,
        False:0
    }
}

# [ 3-A ]
def replace_regexp(string):
    #Correct file encoding
    string=re.sub(r"&amp", " & ", string)
    string=re.sub(r"&lt[; ]", "<", string)
    string=re.sub(r"&gt[; ]", ">", string)

    #Recover "previous" markers
    string=re.sub(r"<.*?>", "<DECIMAL>", string)

    #URLs
    string=re.sub(r"([Hh][Tt][Tt][Pp][Ss]?://|[Ww]{3}\.)([A-Za-z0-9_ -]+\.)+[A-Za-z]{2,5}[A-Za-z0-9/_?=-]*", "<URL>", string)

    #Phone
    string=re.sub(r"\+?[0-9][0-9 -]{3,}[0-9]\+?", "<PHONE>", string)

    #Prices
    string=re.sub(r"\$[0-9]+([,\.][0-9]+)?", "<PRICE>", string)
    string=re.sub(r"[0-9]+p", "<PRICE>", string)

    #Remove useless punctuation
    string=re.sub(r"[\.\*#\\,\?!:;\"]", " ", string)

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

def load_stopwords():
    print("Loading stopwords...")
    with open("stopwords.txt") as stopwords_file:
        for word in stopwords_file.readline().split(','):
            stopwords.append(word[1:-1])
    print("Stopwords loaded")
def complete_train():
    #Loading and preprocessus training cases
    print("\nLoading and preprocess training cases...")
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

    #Training knowledge base
    print("\nTraining knowledge base...")
    train(labels, strings)
    print("Knowledge base trained")

    #Update total probability
    ham=float(category_count["ham"])/sum(category_count.values())
    spam=float(category_count["spam"])/sum(category_count.values())
    return (ham, spam)

# [ 3-F ]
def classify(string):
    words=do_stemming(filter_stopwords(replace_regexp(string), stopwords))
    p_string_ham=1.
    p_string_spam=1.
    for word in words:
        if word in vocab.keys():
            p_word=float(vocab[word])/sum(vocab.values())

            p_string_given_ham=float(category_count_word["ham"].get(word, 0))/category_count["ham"]
            p_string_given_spam=float(category_count_word["spam"].get(word, 0))/category_count["spam"]

            if(p_string_given_ham>0):
                p_string_ham*=p_string_given_ham/p_word
            if(p_string_given_spam>0):
                p_string_spam*=p_string_given_spam/p_word

    if(p_string_spam>p_string_ham):
        return "spam"
    else:
        return "ham"


#Training loading
load_stopwords()
(p_ham, p_spam) = complete_train()

#Test cases
print("\nRunnin tests...")
with open("test") as test_file:
    for line in test_file:
        (label,string) = line.split('|', 1)
        predicted_label=classify(string)

        is_correct=(label==predicted_label)

        test_sorting[label][is_correct]+=1
print("Tests ran")

#Precision/recall/f1 computation
precis_ham=float(test_sorting["ham"][True])/(test_sorting["ham"][True]+test_sorting["ham"][False])
recall_ham=float(test_sorting["ham"][True])/(test_sorting["ham"][True]+test_sorting["spam"][False])
f1meas_ham=2*precis_ham*recall_ham/(precis_ham+recall_ham)
precis_spam=float(test_sorting["spam"][True])/(test_sorting["spam"][True]+test_sorting["spam"][False])
recall_spam=float(test_sorting["spam"][True])/(test_sorting["spam"][True]+test_sorting["ham"][False])
f1meas_spam=2*precis_spam*recall_spam/(precis_spam+recall_spam)

#Print result
print("\nPrecision of ham")
print(precis_ham)
print("Recall of ham")
print(recall_ham)
print("f1-measure of ham")
print(f1meas_ham)
print("\nPrecision of spam")
print(precis_spam)
print("Recall of spam")
print(recall_spam)
print("f1-measure of spam")
print(f1meas_spam)
