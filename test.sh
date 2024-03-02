n=$#

python3 main.py $*

g++ main.cpp

./a.out eggs.csv

jgraph -P test.jgr | ps2pdf - | convert -density 300 - -quality 100 eggs.jpg

exit 0

