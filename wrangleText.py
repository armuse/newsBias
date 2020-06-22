import pandas as pd
import string
from nltk.tokenize import word_tokenize #splits words and punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

articles = pd.read_csv('metadata.csv')
articles = articles.drop(columns = ['copyright','Authors','ArticleType','companies','documentType','language','languageOfSummary','placeOfPublication','entryDate','year','startPage','Database'])
articles.head()

#lower title and subjectTerms
articles['Title'].str.lower()
articles['subjectTerms'].str.lower()

#Add boolean for crime-topic or not
articles['sentiment'] = pd.Series(0) #0 for netural, 1 for crime etc related 

#this removes numbers too - what about COVID-19?
articles['Title'] = articles['Title']

print(articles)

# articles['sentiment'] = articles.apply(lambda row: row[''])

#separate word by space
#word_tokens = word_tokenize(input)
#print(word_tokens)
#get stop words
#stop_words = set(stopwords.words('english'))
#remove punctuation
#no_punctuation = [word.lower() for word in word_tokens if word not in punctuations ] #.isalpha(), .isalnum() but hypens removed
#remove stop words
#stripped_article = [word for word in no_punctuation if not word in stop_words]
#remove 'alec'
#lemmaziation
#stemming

#print remaining:
#print(stripped_article)
