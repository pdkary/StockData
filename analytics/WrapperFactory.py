import datetime

from resources.CustomLibs.TiingoIEXHistoricalReader import TiingoIEXHistoricalReader
import resources.resources as rs
from analytics import StockVectorWrapper
import glob
import os

extension = "csv"
csvdir = os.pardir + '/*.{}'.format(extension)


class WrapperFactory:
    def __init__(self):
        self.end = datetime.datetime.now()
        self.start = self.end - datetime.timedelta(days=4)
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
        out = []
        try:
            new_symbols = [x for x in self.symbols if x not in self.csvs]
            old_symbols = [x for x in self.symbols if x in self.csvs]
            if len(new_symbols):
                data = TiingoIEXHistoricalReader(
                    symbols=new_symbols,
                    start=self.start,
                    end=self.end,
                    api_key=rs.APIKEY).read()
                for x in new_symbols:
                    d = data.loc[x, :]
                    remove = d.loc[self.end.day]
                    close = d['close'].iloc[0]
                    d.drop(remove.index)
                    out.append(StockVectorWrapper(d, x, close))

            if len(old_symbols):
                out += [StockVectorWrapper(os.path.abspath(csvdir[:-5] + x + '.csv'), x, 0) for x in old_symbols]
        except TypeError:
            print("You have run out of your hourly allocation to Tiingo, please try again later")

        return out
