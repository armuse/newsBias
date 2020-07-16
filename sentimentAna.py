import string
import glob
from random import seed
from random import sample
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
        #print(dict([word,True] for word in article) )
		yield dict([word,True] for word in article )

def get_all_words(articles):
    for article in articles:
        for word in article:
            yield word

if __name__ == "__main__":

    #town = 'Baldwin' - generalize to multiple towns soon
    negFiles = glob.glob('data/Baldwin-neg/*.txt')
    posFiles = glob.glob('data/Baldwin-pos/*.txt')

    neg_articles = []
    pos_articles = []

    for file in negFiles: #these are true positives/negative sentiment
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
