def townNaming(town=''):

	town_names = ['Baldwin','Freeport','Oceanside']
	while not town:
		town = input("Which town would you like to process the data for? ")
		if town in town_names:
			print("Now Splitting "+town)
		else: print("You didn't enter a valid town, please try again")
	return town

def reinitializeFile():
	docId = '0'
	title = 'refill'
	fullText = 'refill'
	subject = 'refill'

def breakdownFile(town):

	inFile = 'ProQuestDocuments-'+town+'-1000.txt'
	input = open(inFile,'r')

	outputDir = 'data/'+town+'/'
	title = 'empty'
	fullText = 'empty'
	subject = 'empty'

	try:
		docId = '0'
		counter = 0
		for line in input:
			#if line[0:3] == '___': #this marks a new record, record previous and clear saved info 
			if line[0:3] == 'Tit': # title
				title = line
			elif line[0:3] == 'Ful': # fullText
				fullText = line
				counter += 1
			elif counter > 0:
				if line[0:3] == 'Sub': #subject
					subject = line
					counter = 0
				elif line[0:6] == 'CAPTION' or line[0:5] == 'CREDIT': continue #don't save Caption or Credit info
				else: fullText += line
			elif line[0:8] == 'ProQuest': #add document ID aka bookkeeping
				docId = line[22:-2] #there's a '\n' at the end
				outputName = town+'-'+docId+'.txt'
				out = open(outputDir+outputName, 'w')
				out.write(title+'\n')
				out.write(fullText+'\n')
				out.write(subject+'\n')
				out.close()
				counter = 0
				reinitializeFile()
			else: continue #information we don't need to save

	finally:
		input.close()

def main():
	town = townNaming()
	breakdownFile(town)

main()
