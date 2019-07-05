import os
from src.main.data.WrapperFactory import WrapperFactory
import datetime

symbols = ['AMZN']


def getNow():
    now = datetime.datetime.now()
    return now


if __name__ == '__main__':
    start = getNow()
    vector_list = WrapperFactory().setSymbols(symbols).build

    end = getNow()
    print("end: ", end, "\t start:", start)
    print("Time Elapsed: ", (end - start).total_seconds(), "s")

    for x in vector_list:
        x.df.to_csv(os.pardir + r'/' + x.name + r'.csv')
        x.vectorize()
        print(x.mean_vector, '\n\n', '-' * 75, '\n\n', x.std_vector)
        # ES = x['close']
