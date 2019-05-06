"""
Watchlist class
"""

class Watchlist:
    """
    Watchlist for stock info
    """
    def __init__(self, name, tickers=[]):
        self.name = name
        self.tickers = tickers
