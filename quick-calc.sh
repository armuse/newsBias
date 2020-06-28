#!/bin/bash/


foundTown = false

while [foundTown]
do
  echo "Which town do you want stats for?"
  read town
  if [$town != "Baldwin" and $town != "Freeport" and $town != "Oceanside" and $town != "Rockville" ]
  then
    echo "I do not know which town you are talking about"
  else
    foundTown = true
  fi
done

echo "Name of output file"
read filename

grep $foundTown $foundTown +'/'+ $foundTown +'-edited' > filename
