import string
import glob
from numpy import random
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifer
classifier = NaiveBayesClassifer.train(train_data)

town = 'Freeport' #'Baldwin' #

def readIn(filename): #return corpus per entry
    tmp = open(file[:-1],'r')
    list_of_words = []
    for line in tmp:
        for word in line.split():
            list_of_words.append(word)
    return list_of_words



negFiles = open('input-neg.txt','r')
posFiles = open('input-pos.txt','r')
neuFiles = open('input.txt','r')

negFiles = glob.glob('data/Baldwin-edited/*True*')
posFiles = glob.glob('data/Baldwin-edit/*False*')

neg_words = []
pos_words = []

#make dictionary
#split training and testing datasets


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
all_neutral_words = get_all_words(neu_words)

#get frequency distributions
freq_dist_pos = FreqDist(all_pos_words)
print(freq_dist_pos.most_common(20))
freq_dist_neg = FreqDist(all_neg_words)
print("Now Neg words")
print(freq_dist_neg.most_common(20))
print('Now All combined')
print(freq_dist_neg.most_common(20))

#create dictionary with words, assigning positive/negative
def get_article_for_model(list):
    for article_tokens in list:
        yield dict([token, True] for token in article_tokens)
##??? Why are they all true?
##SVM here
