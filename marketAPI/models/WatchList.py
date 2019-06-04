"""
Watchlist class
"""

class Watchlist:
    """
    Watchlist for stock info
    """
    def __init__(self, name, owner_id, tickers=[]):
        self.name = name
        self.tickers = tickers
        self.owner_id = owner_id

    def __repr__(self):
        return {
            "name": self.name,
            "tickers": self.tickers,
            "owner_id": self.owner_id
        }

    def add_ticker(self, ticker):
        pass

    def remove_ticker(self, ticker):
        self.tickers.remove(ticker)

    def display_prices(self):
        for ticker in self.tickers:
            # TODO
            pass
