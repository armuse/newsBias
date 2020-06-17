import pandas as pd 

#data retrieved from 2018 census on https://censusreporter.org/

data = {'Name': ['Baldwin','Baldwin Harbor','Freeport','Oceanside','Rockville Centre'],
		'Population': [25134,7690,43128,31185,24442],
		'Square Miles': [3.,1.2,4.6,4.9,3.3]
		'Per White': [34,43,25,85,79],
		'Per Black': [35,28,29,1,6],
		'Per Hispanic': [25,22,42,11,11],
		'Per Asian': [3,5,2,2,3],
		'Per 2+': [3,2,3,0,1]
	
	}

towns = pd.DataFrame(data, columns = ['Name','Population','Square miles','Per White','Per Black','Per Hispanic', 'Per Asian','Per 2+'])

#combine Baldwin and Baldwin Harbor