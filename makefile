.PHONY: 1
1:
	sh test.sh GME AMD BBBY 2020-01-01 2023-02-1 s
2: 
	sh test.sh nvda 2021-01-01 2024-02-1 s
3: 
	sh test.sh nvda aapl googl msft hd AMD 2010-01-01 2024-02-28 b
4:
	sh test.sh tsm 2000-01-01 2024-02-28 b
5:
	sh test.sh wmt tgt ko bf BAC PG JNJ 2019-1-1 2022-01-01 s 
clean:
	rm -f *.csv *.jpg *.jgr *.exe *.out