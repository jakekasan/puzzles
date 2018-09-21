from nltk.corpus import movie_reviews
import nltk
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
import random

documents = [(list(movie_reviews.words(fileid)), category)
                for category in movie_reviews.categories()
                for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def get_features(document):
    document_words = set(document)
    return [1 if word in document_words else 0 for word in word_features]

def get_features_nltk(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

def sklearn_way(documents):
    featuresets = [(get_features(doc)+[label]) for (doc,label) in documents]
    labels = ["x_{}".format(x) for x in range(2000)]
    labels.append("y")


    df = pd.DataFrame(featuresets,columns=labels)

    #df["y"] = df["y"].apply(lambda x: 1 if x == "pos" else 0)

    x_train, x_test, y_train, y_test = train_test_split(df.drop("y",axis=1),df["y"],train_size=0.8)


    gnb = GaussianNB()
    bnb = BernoulliNB()
    mnb = MultinomialNB()

    gnb.fit(x_train,y_train)
    bnb.fit(x_train,y_train)
    mnb.fit(x_train,y_train)

    print(gnb.score(x_test,y_test))
    print(bnb.score(x_test,y_test))
    print(mnb.score(x_test,y_test))
    return

def nltk_way(documents):
    featuresets = [(get_features_nltk(d),c) for (d,c) in documents]
    train_set,test_set = featuresets[100:], featuresets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print(nltk.classify.accuracy(classifier,test_set))
    return

#nltk_way(documents)

sklearn_way(documents)
nltk_way(documents)