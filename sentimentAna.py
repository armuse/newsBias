import string
import glob
from numpy import random
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier

def readIn(filename): #return corpus per entry
    tmp = open(file,'r')
    list_of_words = []
    for line in tmp:
        for word in line.split():
            list_of_words.append(word)
    return list_of_words

def get_all_words_for_model(articles): #yields all the words in above lists
	for article in articles:
		yield dict([word,True] for word in article )

def get_all_words(articles):
    for article in articles:
        for word in article:
            yield word

def getTrainingDataset(positiveDataset,negativeDataset):
    random.shuffle(positiveDataset)
    posTrainFrac = int(len(positiveDataset)*0.9)
    negTrainFrac = int(len(negativeDataset)*0.9)
    train_data = positiveDataset[:posTrainFrac] + negativeDataset[:negTrainFrac]
    random.shuffle(train_data)
    return train_data

def getTestDataset(positiveDataset,negativeDataset):
    random.shuffle(negativeDataset)
    posTrainFrac = int(len(positiveDataset)*0.9)
    negTrainFrac = int(len(negativeDataset)*0.9)
    test_data = positiveDataset[posTrainFrac:] + negativeDataset[:negTrainFrac]
    random.shuffle(test_data)
    return test_data

def townNaming(town=''):

	town_names = ['Baldwin','Freeport','Oceanside']
	while not town:
		town = input("Which town would you like to process the data for? ")
		if town in town_names:
			print("Now Splitting "+town)
		else: print("You didn't enter a valid town, please try again")
	return town

if __name__ == "__main__":
    #town = townNaming()
    town = 'Baldwin'

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
    #freq_dist_pos = FreqDist(pos_temp)
    #print("Most Common Positive Words")
    #print(freq_dist_pos.most_common(20))
    #freq_dist_neg = FreqDist(neg_temp)
    #print("Most Common Negative Words")
    #print(freq_dist_neg.most_common(20))

    #get all words in dict format for training
    neg_words = get_all_words_for_model(neg_articles)
    pos_words = get_all_words_for_model(pos_articles)

    positiveDataset = [(article_dict, "Positive") for article_dict in pos_words]
    negativeDataset = [(article_dict, "Negative") for article_dict in neg_words]

    train_data = getTrainingDataset(positiveDataset,negativeDataset)
    test_data = getTestDataset(positiveDataset,negativeDataset)

    #train Naive Bayes Classifer
    classifier = NaiveBayesClassifier.train(train_data)

    #print out Accuracy and most informative feature
    print("Accuracy is: ", classify.accuracy(classifier, test_data))
    print(classifier.show_most_informative_features(20))
