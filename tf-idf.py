
import string
import glob
from pathlib import Path
import pandas as pd
from numpy import random
import math
from nltk.tokenize import word_tokenize
from nltk.text import TextCollection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

town = 'Freeport'

def readIn(filename): #return corpus per entry
    tmp = open(file[:-1],'r')
    list_of_words = []
    for line in tmp:
        for word in line.split():
            list_of_words.append(word)
    return list_of_words

def get_article_for_model(list):
    for article_tokens in list:
        yield dict([token, True] for token in article_tokens)

def get_all_words(list_of_words): #yields all the words in above lists
    for list in list_of_words:
        for word in list:
            yield word

#inputFiles = glob.glob('data/Baldwin-edited/*')
inputFiles = glob.glob('data/Freeport-edited/*')

#print(inputFiles)

#Files = open('input.txt','r')

all_articles = []

for file in inputFiles:
    with open(file) as f:
        txt_file_as_string = f.read();
    all_articles.append(txt_file_as_string)

def create_dict_articles(inputFiles):
    all_articles = {}
    with open(file) as f:
        txt_file_as_string = f.read();
        all_articles[file] = txt_file_as_string
    return all_articles


def create_freq_matrix(articles):
    frequency_matrix = {}

    for article in articles:
        freq_table = {}
        words = word_tokenize(article)

        for word in words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
        #save out the top 25 of each article
        frequency_matrix[article[:15]] = freq_table
    return frequency_matrix

def create_tf_matrix(freq_matrix):
    tf_matrix = {}

    for article, f_table in freq_matrix.items():
        tf_table = {}

        count_words_in_article = len(f_table)
        for word, count in f_table.items():
            tf_table[word] = count/count_words_in_article

        tf_matrix[article] = tf_table

    return tf_matrix


def create_art_per_words(freq_matrix):
    word_per_article_table = {}

    for article, f_table in freq_matrix.items():
        for word, count in f_table.items():
            if word in word_per_article_table:
                word_per_article_table[word] += 1
            else:
                word_per_article_table[word] = 1
    return word_per_article_table

def create_idf_matrix(freq_matrix, count_art_per_words, total_articles):
    idf_matrix = {}

    for article, f_table in freq_matrix.items():
        idf_table = {}

        for word in f_table.keys():
            idf_table[word] = math.log10(total_articles / float(count_art_per_words[word]))

        idf_matrix[article] = idf_table

    return idf_matrix

def create_tf_idf_matrix(tf_matrix, idf_matrix):
    tf_idf_matrix = {}

    for (art1, f_table1), (art2, f_table2) in zip(tf_matrix.items(), idf_matrix.items()):
        tf_idf_table = {}

        for (word1, value1), (word2, value2) in zip(f_table1.items(), f_table2.items()):
            tf_idf_table[word1] = float(value1 * value2)

        tf_idf_matrix[word1] = tf_idf_table
    return tf_idf_matrix

def score_articles(tf_idf_matrix) -> dict:
    articlesValue = {}

    for article, f_table in tf_idf_matrix.items():
        total_score_per_article = 0

        count_words_in_article = len(f_table)
        for word, score in f_table.items():
            total_score_per_article += score

        articlesValue[article] = total_score_per_article / count_words_in_article

    return articlesValue

def find_average_score(values) -> int:
    sumValues = 0
    for entry in values:
        sumValues += values[entry]

    average = (sumValues/ len(values))
    return average

freq_matrix = create_freq_matrix(all_articles)
tf_matrix = create_tf_matrix(freq_matrix)
common_words = create_art_per_words(freq_matrix)
total_articles = len(all_articles)
idf_matrix = create_idf_matrix(freq_matrix, common_words, total_articles)
tf_idf_matrix = create_tf_idf_matrix(tf_matrix, idf_matrix)
values = score_articles(tf_idf_matrix)
threshold = find_average_score(values)

def find_important_words(values):
    inverted = {}
    inverted = {k: v for k, v in sorted(values.items(), key =lambda item: item[1])}
    #highest at end - return only say 10
    return inverted

most_important = find_important_words(values)
print(most_important)

#vectorizer = TfidfVectorizer(max_df = .65, min_df = 1, stop_words = None, use_idf = True, norm = None)
#transformed_documents = vectorizer.fit_transform(all_articles)
#transformed_documents_as_array = transformed_documents.toarray()
#print(len(transformed_documents_as_array))

#Path('./tf_idf_output').mkdir(parents=True, exist_ok=True)
#output_filenames = [str(file).replace('.txt','.csv').replace('data/Baldwin','tf_idf_output') for file in Files]
#for counter, doc in enumerate(transformed_documents_as_array):#
##    tf_idf_tuples = list(zip(vectorizer.get_feature_names(), doc))
#    one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples, columns=['term', 'score']).sort_values(by='score', ascending=False).reset_index(drop=True)
#    print(one_doc_as_df)
    #one_doc_as_df.to_csv(output_filenames[counter])
#print(corpus)
#tfidf = TfidfVectorizer()
##corpus = tfidf.fit_transform(corpus)
##cv = CountVectorizer()
#word_count_vector = cv.fit_transform(corpus)
#print(word_count_vector.shape)
#fidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
#tfidf_transformer.fit(word_count_vector)

#df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
#df_idf.sort_values(by=['idf_weights'])

#print(df_idf.head())
