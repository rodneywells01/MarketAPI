"""
Watchlist class
"""

class Watchlist:
    """
    Watchlist for stock info
    """
    def __init__(self, name, tickers=[], owner_id):
        self.name = name
        self.tickers = tickers
        self.owner_id 

    def __repr__(self): 
        return {
            "name": self.name, 
            "tickers": self.tickers, 
            "owner_id": self.owner_id
        }

    def add_ticker(ticker): 
        

    def remove_ticker(ticker): 
        self.tickers.remove(ticker)

    def display_prices(): 
        for ticker in tickers
