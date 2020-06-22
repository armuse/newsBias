
input = open('ProQuestDocuments-2020-06-18.txt','r')

town = 'Baldwin' #'Freeport', 'Oceanside', 'Rockville'
outDir = 'data/'+town+'/'
title = 'empty'
text = 'empty'
subject = 'empty'

try:
    docId = '0'
    counter = 0
    for line in input:
        if line[0:3] == '___':
            #this marks a new record, record previous and clear saved info
            outputName = town+'-'+docId+'.txt'
            out = open(outDir+outputName, 'w')
            out.write(title+'\n')#+title
            out.write(text+'\n')#+text
            out.write(subject+'\n')#+subject
            out.close()
            docId = '0'
            title = 'refill'
            text = 'refill'
            subject = 'refill'

        elif counter > 0:  #add rest of full text
            if line[0:3] == 'Sub': #add subject terms
                counter = 0
                subject = line
            elif line[0:3] == 'CAP' or line[0:3] == 'CRE': continue
            else: text += line
        elif line[0:3] == 'Tit': #add title
            title = line
        elif line[0:3] == 'Ful': #start adding full text
            text = line
            counter = 1
        elif line[0:3] == 'Pro': #add document ID aka bookkeeping
            docId = line[22:-2] #there's a '\n' at the end
        else: continue #information we don't need to save


finally:
    input.close()
