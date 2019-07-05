import datetime
from src.resources.CustomLibs.TiingoIEXHistoricalReader import TiingoIEXHistoricalReader
import src.resources.resources as rs
from src.main.data.StockVectorWrapper import StockVectorWrapper


class WrapperFactory:
    def __init__(self):
        self.end = datetime.datetime.now()
        self.start = self.end - datetime.timedelta(days=7)
        self.symbols = []
        self.key = rs.APIKEY

    def setStart(self, start):
        self.start = start
        return self

    def setEnd(self, end):
        self.end = end
        return self

    def setSymbols(self, symbols):
        self.symbols = symbols
        return self

    def build(self):
        data = TiingoIEXHistoricalReader(
            symbols=self.symbols,
            start=self.start,
            end=self.end,
            api_key=rs.APIKEY).read()

        return [StockVectorWrapper(data.loc[x, :], x) for x in self.symbols]
