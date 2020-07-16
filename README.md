# newsBias
Goal: exploring news bias in local reporting over the last 5 years (2015-2020)

Instructions so far (uses python3):
python splitRecords.py
python wrangleText.py

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

Approximately 3500-4000 articles per town in 5 years
Have ~1k articles per town right now, train/test 80/20

Following tutorial at: https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
