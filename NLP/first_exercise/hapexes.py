#!/usr/bin/env python3

import os
import re
from collections import Counter

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer



def read_file(filename):
    raw_string = ""

    with open(filename,"r") as f:
        raw_string = f.read()

    return raw_string

def get_tokens(string):

    string = re.sub(r'[\W\s]'," ",string)

    return word_tokenize(string.lower())
    

def get_hapaxes(tokens):

    counter = Counter(tokens)
    
    return [x for x,y in counter.items() if y == 1]
    

def get_hapaxes_stems(tokens):

    stemmer = SnowballStemmer("english")

    stems = [stemmer.stem(token) for token in tokens]
    
    counts = nltk.FreqDist(stems)

    return counts.hapaxes()


def get_hapaxes_lemms(tokens):

    tagged = nltk.pos_tag(tokens)

    tagged = [(word,pt_to_wn(tag)) for (word,tag) in tagged]

    lemmer = WordNetLemmatizer()

    lemmas = [lemmer.lemmatize(token,pos) for (token,pos) in tagged]

    return get_hapaxes_stems(lemmas)

def pt_to_wn(pos):

    from nltk.corpus.reader.wordnet import NOUN, VERB, ADJ, ADV

    pos = pos.lower()

    if pos.startswith("jj"):
        tag = ADJ
    elif pos == "md":
        tag = VERB
    elif pos.startswith("rb"):
        tag = ADV
    elif pos.startswith("vb"):
        tag = VERB
    elif pos == "wrb":
        tag = ADV
    else :
        tag = NOUN

    return tag


def main():
    filename = "./data.txt"

    # read text
    raw_string = read_file(filename)

    # get tokens
    tokens = get_tokens(raw_string)

    word_hapaxes = get_hapaxes(tokens)
    stem_hapaxes = get_hapaxes_stems(tokens)
    lemm_hapaxes = get_hapaxes_lemms(tokens)

    print("Word Hapaxes:\n",word_hapaxes)
    print("Stem Hapaxes:\n",stem_hapaxes)
    print("Lemm hapaxes:\n",lemm_hapaxes)


if __name__ == '__main__':
    main()