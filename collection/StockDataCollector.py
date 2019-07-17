import utils.utils as utils


class StockDataCollector:

    def __init__(self):
        pass

    @property
    def sp500(self):
        return utils.save_sp500_tickers()
