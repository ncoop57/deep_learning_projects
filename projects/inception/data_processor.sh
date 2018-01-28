#! /bin/bash

letters=('A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y')
users=('1' '2' '3' '4' '5' '6' '7')

cd ./data

for i in "${letters[@]}"
do
  cd /home/nathan/projects/machine_learning/tensorflow/projects/inception/data/$i
  counter=1
  for u in "${users[@]}"
  do
    cd ./user_$u/
#    echo $(pwd)
    names=($(ls))
#    echo $names
    cd ..
#    echo $(pwd)

    for l in "${names[@]}"
    do
      cp ./user_$u/$l "${l}-${counter}".jpg
#      echo $l
    done
    let counter=counter+1
  done
  #echo letter: $i
  cd ..
done
