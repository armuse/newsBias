import subprocess
import string
from nltk.tokenize import word_tokenize #splits words and punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

town_names = ['Baldwin','Freeport','Oceanside','Rockville Centre']
town = ''
while not town:
    town = input("Which town would you like to wrangle the text for? ")
    if town in town_names:
        print("Now Splitting "+town)
    else: print("You didn't enter a valid town, please try again")

#create input file with shell commands
cmd = 'ls data/'+town+' > input.txt'
subprocess.run(cmd, shell=True)

#inFile = 'ProQuestDocuments-'+town+'-1000.txt'
#input = open(inFile,'r')

inFiles = open('input.txt','r') #ls data/X/* > input.xt

neg = ['criminal','firearms','murders','manslaughter','arrests','burglary','robbery','violence','cocaine','heroin','police']
#victimization, missing persons,
outDir = 'data/'+town+'-edited/'

stop_words = set(stopwords.words('english'))

for article in inFiles: #each article is its own line
    name = 'data/'+town+'/'+article
    file = open(name[:-1],'r') #there's \n at end of line #used to be article
    keep = True
    truthNeg = False
    edited = []

    for line in file:
        line = line.lower()
        if 'alec' in line: #Alec Baldwin is NOISE
            keep = False
            continue
        if line[0:3] == 'sub': #check subject terms for truth classification
            subjects = word_tokenize(line)
            #print(subjects)
            for term in neg:
                if term in subjects:
                    truthNeg = True
                    continue #one true, all True
            continue #don't save out subject line
        #save only title, full text and subject
        elif (line[0:6] == 'credit' or line[0:4] == 'illu'
            or line[0:6] == 'author' or line[0:5] == 'https'
            or line[0:11] == 'publication' or line[0:8] == 'abstract'
            or line[0:6] == 'refill'): #cases in python?!?!
            continue #skip non article information
        if (line[0:5] == 'title'): #remove label title
            line = line[7:]
        if (line[0:9] == 'full text'): #remove label full text
            line = line[11:]
        word_tokens = word_tokenize(line)
        for word in word_tokens: #keep basic words
            if word.isalpha():
                if not word in stop_words:
                    #print(lemmatizer.lemmatize(word))
                    edited.append(lemmatizer.lemmatize(word))
    #bag of words vectors?

    if keep:
        outName = outDir+article[:-5]+'-'+str(truthNeg)+'.txt'
        outFile = open(outName,'w')
#        outFile.write(edited)
        for i in range(len(edited)):
            outFile.write(edited[i]+' ')
        outFile.close()
    file.close()

    #finally:
inFiles.close()
