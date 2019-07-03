import pandas as pd
import numpy as np

class StockDataFrame(pd.DataFrame):
    def addbbhm(self):
        bbSeries = self['bb_high_indicator']
        close_max = pd.Series.max(self['close'])
        close_min = pd.Series.min((self['close']))
        range = close_max - close_min
        self["bb_high_indicator_times_mean"] = pd.Series()
        i = 0
        for j in bbSeries.iteritems():
            mean = self['close_running_mean'].iloc[i]
            self["bb_high_indicator_times_mean"].iat[i] = mean + j[1]*range
            i+=1

    def add_running_mean_and_std(self, strColumn):
        mean_name = strColumn + "_running_mean"
        std_name = strColumn + "_running_std"
        plus_std = strColumn + "_plus_std"
        minus_std = strColumn + "_minus_std"
        count = 1.0
        sum = 0
        self[mean_name] = pd.Series()
        self[std_name] = pd.Series()
        self[plus_std] = pd.Series()
        self[minus_std] = pd.Series()
        for i in range(len(self.index)):
            sum += self[strColumn].iloc[i]
            self[mean_name].iat[i] = sum / count
            self[std_name].iat[i] = self[strColumn][:i].std() / count
            self[plus_std].iat[i] = self[strColumn].iloc[i] + self[strColumn][:i].std()
            self[minus_std].iat[i] = self[strColumn].iloc[i] - self[strColumn][:i].std()
            count += 1

    def fft(self,strColumn):
        newCol = strColumn + "_fft"

        matrix = self[strColumn].values
        print(cnp.fft.fft(matrix)) # these come through as imaginary numbers, gotta convert to degre mm2 m,,le
        self[newCol] = np.fft.fft(matrix)
