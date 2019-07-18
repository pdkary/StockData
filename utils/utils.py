import datetime
import bs4 as bs
import pickle
import requests
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

def combine_dict(d1,d2):
    keyset1 = set(d1.keys())
    keyset2 = set(d2.keys())
    intersection = keyset1.intersection(keyset2)
    twonique = np.setdiff1d(keyset1,keyset2)
    for x in intersection:
        d1[x] += d2[x]
    for x in twonique:
        d1[x] = d2[x]
    return d1