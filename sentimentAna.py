import string
from numpy import random
from nltk import FreqDist

def readIn(filename): #return corpus per entry
    tmp = open(file[:-1],'r')
    list_of_words = []
    for line in tmp:
        for word in line.split():
            list_of_words.append(word)
    return list_of_words

negFiles = open('input-neg.txt','r')
posFiles = open('input-pos.txt','r')

neg_words = []
pos_words = []

for file in negFiles: #these are true positives/negative sentiment
    neg_words.append(readIn(file))

for file in posFiles:
    pos_words.append(readIn(file))

def get_all_words(list_of_words): #yields all the words in above lists
    for list in list_of_words:
        for word in list:
            yield word

all_neg_words = get_all_words(neg_words)
all_pos_words = get_all_words(pos_words)

#get frequency distributions
freq_dist_pos = FreqDist(all_pos_words)
print(freq_dist_pos.most_common(20))
freq_dist_neg = FreqDist(all_neg_words)
print("Now Neg words")
print(freq_dist_neg.most_common(20))

#create dictionary with words, assigning positive/negative
def get_article_for_model(list):
    for article_tokens in list:
        yield dict([token, True] for token in article_tokens)
##??? Why are they all true?
##SVM here 
