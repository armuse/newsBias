import string
from numpy import random

negFiles = open('input-neg.txt','r')
posFiles = open('input-pos.txt','r')

for file in negFiles: #these are true positives
     = open(file[:-1],'r') #there's \n at end of line
