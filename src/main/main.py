from src.main.data.WrapperFactory import WrapperFactory
import datetime
import bs4 as bs
import pickle
import requests
from sklearn.neighbors import NearestNeighbors
import numpy as np


def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    return [x.rstrip() for x in tickers[1::5]]


def getNow():
    now = datetime.datetime.now()
    return now


if __name__ == '__main__':
    symbols = save_sp500_tickers()
    start = getNow()
    wrapper_list = WrapperFactory().setSymbols(symbols).setStart(getNow() - datetime.timedelta(days=3)).as_list

    vector_list = [x.vector for x in wrapper_list]
    vector_arr = np.ndarray((len(vector_list), vector_list[0].shape[0]))
    for x in vector_list:
        np.append(vector_arr, x)

    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(vector_arr)
    distances, indices = nbrs.kneighbors(vector_arr)
    end = getNow()
    print("Time Elapsed: ", (end - start).total_seconds(), "s")
    for x in range(len(indices)):
        print(symbols[indices[x][0]], symbols[indices[x][1]], distances[x][1])
