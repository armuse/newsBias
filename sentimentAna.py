import string
import glob
from random import seed
from random import sample
from numpy import random
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier

#accuracy is ~65% for Baldiwn - check Freeport & Oceanside
#add precision, recall, F1 etc
#try 10 k-fold instead of single train-test split
#test removing low frequency words
#test weighting by TF IDF

#once happy - productionize/pickle

def readIn(filename): #return corpus per entry
    tmp = open(file,'r')
    list_of_words = []
    for line in tmp:
        for word in line.split():
            list_of_words.append(word)
    return list_of_words

def get_all_words_for_model(articles): #yields all the words in above lists
	for article in articles:
        #print(dict([word,True] for word in article) )
		yield dict([word,True] for word in article )

def get_all_words(articles):
    for article in articles:
        for word in article:
            yield word

if __name__ == "__main__":
    town_names = ['Baldwin','Freeport','Oceanside','Rockville Centre']
    town = ''
    while not town:
        town = input("Which town would you like to wrangle the text for? ")
        if town in town_names:
            print("Now Splitting "+town)
        else: print("You didn't enter a valid town, please try again")

    negFiles = glob.glob('data/'+town+'-edited/*True*.txt')
    posFiles = glob.glob('data/'+town+'-edited/*False*.txt')

    neg_articles = []
    pos_articles = []

    for file in negFiles:
        neg_articles.append(readIn(file))
    for file in posFiles:
        pos_articles.append(readIn(file))

    #get all of the words to calculate frequency #s
    neg_temp = get_all_words(neg_articles)
    pos_temp = get_all_words(pos_articles)

    #get frequency distributions
    freq_dist_pos = FreqDist(pos_temp)
    print("Most Common Positive Words")
    print(freq_dist_pos.most_common(20))
    freq_dist_neg = FreqDist(neg_temp)
    print("Most Common Negative Words")
    print(freq_dist_neg.most_common(20))

    #get all words in dict format for training
    neg_words = get_all_words_for_model(neg_articles)
    pos_words = get_all_words_for_model(pos_articles)

    positive_dataset = [(article_dict, "Positive") for article_dict in pos_words]
    negative_dataset = [(article_dict, "Negative") for article_dict in neg_words]

    dataset = positive_dataset + negative_dataset

    #randomize calculate train/test split of dataset
    random.shuffle(dataset)
    trainFrac = int(len(dataset)*0.9)

    train_data = dataset[:trainFrac]
    test_data = dataset[trainFrac:]

    #train Naive Bayes Classifer
    classifier = NaiveBayesClassifier.train(train_data)

    #print out Accuracy and most informative feature
    print("Accuracy is: ", classify.accuracy(classifier, test_data))
    print(classifier.show_most_informative_features(20))
