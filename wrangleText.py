import string
from nltk.tokenize import word_tokenize #splits words and punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

inFiles = open('input.txt','r') #ls data/X/* > input.xt

neg = ['criminal','firearms','murder','manslaughter','arrests','burglary','robbery','violence','police']
#victimization, missing persons,
outDir = 'data/Baldwin-edited'

stop_words = set(stopwords.words('english'))

for article in inFiles: #each article is its own line
    file = open(article[:-1],'r') #there's \n at end of line
    keep = True
    truthNeg = False
    edited = []

    for line in file:
        line = line.lower()
        if 'alec' in line: #Alec Baldwin is NOISE
            keep = False
            continue
        if line[0:3] == 'sub': #check subject terms for truth classification
            print(line)
            for term in neg:
                if term in line:
                    truthNeg = True
                    continue #one true, all true
        #save only title, full text and subject
        elif (line[0:6] == 'credit' or line[0:4] == 'illu'
            or line[0:6] == 'author' or line[0:5] == 'https'
            or line[0:11] == 'publication'):
            continue #skip non article information
        word_tokens = word_tokenize(line)
        no_punctuation = [word.isalpha() for word in word_tokens]
        remove_stop = [word for word in no_punctuation if not word in stop_words]
        lemmed_words = [lemmatizer.lemmatize(word) for word in remove_stop]
        #remove punctuation
        #remove stop words
        #stem/lemm
        print (lemmed_words)
        #edited.append(+' ')

    if keep:
        outName = outDir+article[12:-5]+'-'+str(truthNeg)+'.txt'
        outFile = open(outName,'w')
        outFile.write(lemmed_words)
#        for i in range(len(edited)):
#            outFile.write(edited[i])
        outFile.close()
    file.close()

    #finally:
inFiles.close()
