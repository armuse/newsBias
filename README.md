# newsBias
Goal: exploring news bias in local reporting over the last 5 years (2015-2020)

Instructions so far (uses python3):
python3 splitRecords.py
python3 wrangleText.py
python3 sentimentAnalysis.py

Jupyter notebook of Demographics for further analysis

towns:
Baldwin ( + Baldwin Harbor) NY
Rockville Centre NY
Freeport NY
Oceanside NY

source: Newsday

Null hypothesis: no bias in reporting crimes/others ratio per town

Terms used for identifying crimes (truth dataset):
	crime
	criminal investigation
	fraud
	arrest
	robbery
	firearms
	heroin
	cocaine
	murder
	violence
	manslaughter
	shooting

Have ~1k articles per town right now, train/test 80/20
Goal to improve Accuracy: Approximately 3500-4500 articles per town in 5 years

Following tutorial at: https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
