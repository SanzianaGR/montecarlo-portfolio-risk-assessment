import yfinance as yf
import numpy as np
import pandas as pd

class DataFetcher:

    def __init__(self, symbols, days=252):
        self.symbols = symbols
        self.days = days
   
    def fetch(self):
        
        returns_list = []
        
        for symbol in self.symbols:
            print(f"   {symbol}...", end=" ")
            ticker = yf.Ticker(symbol) # access stock data
            hist = ticker.history(period="1y")
            
            if hist.empty:
                raise ValueError(f"No data for {symbol}")
            
            returns = hist['Close'].pct_change().dropna() # If the price goes from 100 to 105, that's a 5% return. pct_change calculates this for every day
            returns_list.append(returns)
            print(f" {len(returns)} days")
        
        returns_df = pd.concat(returns_list, axis=1, keys=self.symbols)
        returns_df = returns_df.dropna()
        
        print(f"\n Successfully fetched {len(returns_df)} days of data")
        print(f"   Date range: {returns_df.index[0].date()} to {returns_df.index[-1].date()}\n")
        
        return returns_df
    
    