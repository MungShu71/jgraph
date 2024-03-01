# Jgraph

usage: sh test.sh [stock tickers] [fromDate] [toDate] S|B

The shell script command takes in up to seven NASDAQ listed stock tickers, data range, and a S for small or B for big. 

**How it works** 
The shell script calls the Python script ```main.py``` with the command line arguments as input. ```main.py``` does a API request for each stock's data over the given timeframe. This data is written to the csv file ```eggs.csv```. Then ```main.cpp``` reads the CSV file and creates ```test.jgr```. Finally, the shell script compiles the jgr file into ```eggs.jpg```.

For example, when I call:
```
sh test.sh nvda aapl googl msft hd AMD 2010-01-01 2024-02-29 b
```
this is the outputted jpeg image (cropped it manually).
![2010](https://github.com/MungShu71/jgraph/assets/112988109/0dd772c2-34f3-4af3-b1f4-7b76f85e36d8)

```What is S and B in the command line?```

We live in a world where capitalism rules with an iron fist. I originally wrote this over winter break of 2023. At that time I was using a free API called YFINANCE - Stock Market Data. However, after picking Jgraph back up for 494 Lab 1, the API was blocked by a paywall. One dollar a month is a lot of money in this day and age; it can almost pay for 1/3 of a gallon of gas. But since I had start using it before the free plan had depercated, I still had access to a free API token (in fact I have two - one on personal account and one on school account). You are able to freely use it until you hit the daily request limit. 

Because I know people love looking at graphs of stock prices and worrying about hitting the limit to quickly, I found another API to use. This one only retreives data up to three years prior. So, in short, use S if you want data that are more than three years, but use it sparingly. Use B for everything else. 
