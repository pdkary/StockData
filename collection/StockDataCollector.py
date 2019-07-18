import utils.utils as utils
import resources.resources as rs
from resources.CustomLibs.TiingoIEXHistoricalReader import TiingoIEXHistoricalReader
from db.MongoConnector import MongoConnector


class StockDataCollector:

    def __init__(self):
        self.mongo_client = MongoConnector()

    @property
    def sp500(self):
        return utils.save_sp500_tickers()

    def getStocks(self, symbols):
        out = []
        try:
            new_symbols = [x for x in symbols if x not in self.mongo_client.collections]
            old_symbols = [x for x in symbols if x in self.mongo_client.collections]
            out.append()
            if len(new_symbols):
                data = TiingoIEXHistoricalReader(
                    symbols=new_symbols,
                    start=self.start,
                    end=self.end,
                    api_key=rs.APIKEY).read()
            for x in new_symbols:
                d = data.loc[x, :]
                remove = d.loc[self.end.day]
                d.drop(remove.index)
                data = self.mongo_client.db.update_collection(x, d)
                out.append(d)
        except TypeError:
            print("You have run out of your hourly allocation to Tiingo, please try again later")
