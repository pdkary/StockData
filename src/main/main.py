from data.StockVectorWrapper import *
from data.EnhancedSeries import *

symbols = ['AMZN', 'LMT']


def getNow():
    now = datetime.datetime.now()
    return now


if __name__ == '__main__':
    start = getNow()
    vector_list = WrapperFactory().setSymbols(symbols).build()
    end = getNow()
    print("end: ", end, "\t start:", start)
    print("Time Elapsed: ", (end - start).total_seconds(), "s")

    for x in vector_list:
        print('-' * 75)
        ES = x.BBHI
        print(type(ES))
