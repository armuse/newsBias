import subprocess
import string
from nltk.tokenize import word_tokenize #splits words and punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

def townNaming(town=''):

	town_names = ['Baldwin','Freeport','Oceanside']
	while not town:
		town = input("Which town would you like to process the data for? ")
		if town in town_names:
			print("Now Splitting "+town)
		else: print("You didn't enter a valid town, please try again")
	return town

def createInputFile(town):

    command = 'ls data/'+town+' > input.txt'
    subprocess.run(command, shell=True)

def createNegativeTermList():

    negativeTerms = ['criminal','firearms','murders','manslaughter','arrests','burglary',
        'robbery','violence','cocaine','heroin','criminals','murder','firearm']
    return negativeTerms

def writeOutFile(town,article,truthNeg,edited):

    outputDir = 'data/'+town+'-edited/'
    outputName = outputDir+article[:-5]+'-'+str(truthNeg)+'.txt'
    outputFile = open(outputName,'w')
    for i in range(len(edited)):
        outputFile.write(edited[i]+' ')
    outputFile.close()

def createStopWords(town):

    stopWords = set(stopwords.words('english'))
    #add some common yet meaningless words to stop words to remove
    meaningless_words = ['county','nassau','long','island','york',
        'NY','say','go','make','would','get','also','year','one',
        'two','newsday','could']
    stopWords.update(meaningless_words)
    stopWords.update(town)
    return stopWords

def irrelevantInfo(line):
    irrelevant = False
    if (line[0:6] == 'credit' or line[0:4] == 'illu'
        or line[0:6] == 'author' or line[0:5] == 'https'
        or line[0:11] == 'publication' or line[0:8] == 'abstract'
        or line[0:6] == 'refill'): irrelevant = True
    return irrelevant

def noMoreAlec(line):
    if 'alec' in line: #Alec Baldwin is NOISE
        return True
    else: return False

def labelArticles(neg,word_tokens): #True means criminal
    for term in neg:
        if term in word_tokens:
            return True

def main():

    town = townNaming()
    createInputFile(town)

    inFiles = open('input.txt','r')

    lemmatizer = WordNetLemmatizer()
    neg = createNegativeTermList()
    stopWords = createStopWords(town)

    for article in inFiles: #each article is its own line in inFiles

        name = 'data/'+town+'/'+article
        file = open(name[:-1],'r') #there's \n at end of line #used to be article
        keep = True
        truthNeg = False
        edited = []

        for line in file:

            line = line.lower()

            if town == 'Baldwin':
                if noMoreAlec(line):
                    keep = False
                    continue

            checkForIrrelevancy = irrelevantInfo(line)

            if checkForIrrelevancy:
                continue #skip non article information

            if (line[0:5] == 'title'): #remove label title
                line = line[7:]
            if (line[0:9] == 'full text'): #remove label full text
                line = line[11:]

            word_tokens = word_tokenize(line)

            if labelArticles(neg,word_tokens): truthNeg = True

            for word, tag in pos_tag(word_tokens):
                if tag.startswith('NN'):
                    pos = 'n'
                elif tag.startswith('VB'):
                    pos = 'v'
                else:
                    pos = 'a'
                if word.isalpha():
                    lemmed_word = lemmatizer.lemmatize(word,pos)
                    if not lemmed_word in stopWords:
                        edited.append(word)

        if keep:
            writeOutFile(town,article,truthNeg,edited)
        file.close()

    inFiles.close()

main()
