import json
import csv
import requests
import sys
from datetime import datetime as dt
from datetime import date
import time
class Jgraph():
    def __init__(self, *args) -> None:
        self.type = args[-1].upper()

        if self.type == 'S':
            self.url = "https://apistocks.p.rapidapi.com/daily"                                   # free one
        elif (self.type == 'B'):
            self.url = "https://yfinance-stock-market-data.p.rapidapi.com/price-customdate"

        if self.type == 'S': 
            self.querystring = {                                                              # free one
                "symbol": "",
                "dateStart": "",
                "dateEnd": ""
            }

        elif self.type == 'B':
            self.payload = {
                "symbol": "AAPL",
                "end": "2022-04-30",
                "start": "2022-01-01"
            }

        if self.type == 'S': 
            self.headers = {                                                                          # free one
	            "X-RapidAPI-Key": "b43be43a44msh52bc86ffba34392p150d9ajsna0b355819458",
	            "X-RapidAPI-Host": "apistocks.p.rapidapi.com"
            }

        elif self.type == 'B': 
            self.headers = {
        	    "content-type": "application/x-www-form-urlencoded",
        	    "X-RapidAPI-Key": "b43be43a44msh52bc86ffba34392p150d9ajsna0b355819458",
                # "X-RapidAPI-Key": "7d9f925bd4msh0edf07ea60cd181p1ef23ajsn41169cced24b",                             # yvy UNCOMMMENT AND COMMENT OUT TOKEN ABOVE TO USE
        	    "X-RapidAPI-Host": "yfinance-stock-market-data.p.rapidapi.com"
            }

        if self.type == 'S': 
            self.header = ["Ticker", "Date", "Open", "Close", "High", "Low", "Volume", "AdjClose"]            # free one
        
        elif self.type == 'B': 
            self.header = ["Ticker", "Date", "Open", "Close", "High", "Low", "Volume", "Adj Close"]

        self.data = []
        self.maxPrice = 0

        self.tickers = args[:-3]    
        self.range_from = args[-3]
        self.range_to = args[-2]

    def format_date(self):
        def format(date):
            fdate = date.split("-")
            for i in range(len(fdate)):
                fdate[i] = fdate[i].zfill(2)
            return "-".join(fdate)

       
        if self.type == 'S': 
            self.querystring["dateStart"] = format(self.range_from)           # free one
            self.querystring["dateEnd"] = format(self.range_to) 

        elif self.type == 'B': 
            self.payload["start"] = format(self.range_from)
            self.payload["end"] = format(self.range_to)


    def get_days(self):
        if self.type == 'S':
            e = [int(i) for i in self.querystring['dateEnd'].split("-")]            # free one
            s = [int(i) for i in self.querystring['dateStart'].split("-")]            # free one
        
        elif self.type == 'B':
            s = [int(i) for i in self.payload['start'].split("-")]          
            e = [int(i) for i in self.payload['end'].split("-")]
        
        s1 = date(year = s[0], month = s[1], day = s[2])
        e1 = date(year = e[0], month = e[1], day = e[2])
        delta = e1 - s1

        return str(int(delta.days - ((delta.days / 30) * 8)))


             
        
    def format_data(self, data, ticker):
        for index in range(len(data)):
            data[index]["Ticker"] = ticker.upper()
            

            if self.type == 'S':
                data[index]["Date"] = '-'.join(data[index]["Date"].split('-')[::-1])    # free one
            
            elif self.type == 'B':
                data[index]["Date"] = dt.fromtimestamp((data[index]["Date"])/1000).strftime("%d-%m-%Y")

            self.maxPrice = max(self.maxPrice, data[index]['High'])
        return data
        
    
    def request(self,ticker):

        if self.type == 'S':                     
            self.querystring["symbol"] = ticker.upper()                             # free
            response = requests.get(self.url, headers=self.headers, params=self.querystring)
            sub_data = response.json()['Results']  
        elif self.type == 'B':
            self.payload["symbol"] = ticker.upper()   
            response = requests.post(self.url, data=self.payload, headers=self.headers)
            sub_data = response.json()['data']
 

        sub_data = self.format_data(sub_data,ticker)
        
        self.data.append(sub_data)
        

    

    
    def get_data(self):

         for ticker in self.tickers:
              for i in ticker:

              
                (self.request(i))
                time.sleep(2)


    def write_file(self):

        with open('eggs.csv', 'w', newline='') as csvfile:
   
            csvwriter = csv.DictWriter(csvfile, fieldnames= self.header)
            
            csvwriter.writeheader()
         
            csvfile.write(self.get_days())
            csvfile.write("/\n")

            p = self.maxPrice 
            p += 50 - (p % 50)

            csvfile.write(str(int(p)))
            csvfile.write("/\n")

            for row in self.data:
                for i in row:
                    # print(i)

                    csvwriter.writerow(i)


c = Jgraph(sys.argv[1:-2], sys.argv[-3], sys.argv[-2], sys.argv[-1])

                        
c.format_date()

c.get_data()

c.write_file()
