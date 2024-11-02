shuf -n 100 train.csv > train1.csv
grep -v -x -F -f train1.csv train.csv > test1.csv
