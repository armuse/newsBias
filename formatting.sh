#!/bin/bash

filename="ProQuestDocuments-2020-06-18.txt"
#add ability to add together multiple files later
#check for file opening properly

outputFile="condensedNews.csv"

Title #this is positional, not described by x:
abs
date
text
sub
id

while read line; # is a for loop better?
do
  if [[ $line == *"Abstract:"* ]]; then
    abs="${line:9}"

  elif [[ $line == *"Publication Date:"* ]]; then
    date="${line:17}"

  elif [[ $line == *"Full text:"* ]]; then
    text="${line:10}"

  elif [[ $line == *"Subject:"* ]]; then
    sub="${line:8}"

  elif [[ $line == *"ProQuest document ID:"* ]]; then
    id="${line:21}"
  fi


  #separate outputs by
  #xyz;
  if [$line == "____________________________________________________________"]; then
    printf "new record"

    #write out new record to file

#    $id,$Title,$abs,$date,$text,$sub, &> outputFile
    printf '%s\n' id Title abs date text sub | paste -sd ',' >> file.csv

    counter += 1

    continue
  fi
  #next line is title...
  printf $line
done < $filename

echo "Formatted "+counter+" records" #maybe need to do string conversion


#separate terms by carriage returns somehow
