import datetime
from src.resources.CustomLibs.TiingoIEXHistoricalReader import TiingoIEXHistoricalReader
import src.resources.resources as rs
from src.main.data.StockVectorWrapper import StockVectorWrapper
import glob
import pandas as pd
import os

extension = "csv"
csvdir = os.pardir + '/*.{}'.format(extension)


class WrapperFactory:
    def __init__(self):
        self.end = datetime.datetime.now()
        self.start = self.end - datetime.timedelta(days=7)
        self.symbols = []
        self.key = rs.APIKEY
        self.csvs = [x[3:-4] for x in glob.glob(csvdir)]

    def setStart(self, start):
        self.start = start
        return self

    def setEnd(self, end):
        self.end = end
        return self

    def setSymbols(self, symbols):
        self.symbols = symbols
        return self

    @property
    def as_list(self):
        new_symbols = [x for x in self.symbols if x not in self.csvs]
        old_symbols = [x for x in self.symbols if x in self.csvs]
        out = []
        if len(new_symbols):
            data = TiingoIEXHistoricalReader(
                symbols=new_symbols,
                start=self.start,
                end=self.end,
                api_key=rs.APIKEY).read()
            out += [StockVectorWrapper(data.loc[x, :], x) for x in new_symbols]
        if len(old_symbols):
            out += [StockVectorWrapper(os.path.abspath(csvdir[:-5] + x + '.csv'), x) for x in old_symbols]

        return out
