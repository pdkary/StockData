import pandas_datareader as pdr
import resources as rs
import datetime as dt

now = dt.datetime.now()
week_ago = now - dt.timedelta(days=7)
dateFormat = "%Y-%m-%d"

end_time = now.strftime(dateFormat)
start_time = week_ago.strftime(dateFormat)

symbols = ['YHOO']

yahoo = pdr.tiingo.TiingoDailyReader(symbols=symbols, start=start_time, end=end_time, api_key=rs.APIKEY).read()
if __name__ == '__main__':
    print(yahoo)
    print(end_time)
    print('done')
