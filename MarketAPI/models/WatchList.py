class WatchList:
    """
    A watchlist of stocks.
    """

    def __init__(self, name="My WatchList", tickers=[], creator=0):
        self.name = name
        self.tickers = tickers
        self.creator = creator

    def __iter__(self):
        return iter((
            ("name", self.name),
            ("tickers", self.tickers)
            ("creator", self.creator)
        ))

    def __repr__(self):
        return str({"name": self.name, "tickers": self.tickers})
