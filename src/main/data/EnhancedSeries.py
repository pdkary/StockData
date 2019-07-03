import pandas as pd


class EnhancedSeries:

    def __init__(self, series_name, series):
        self.df = pd.DataFrame()
        self.df[series_name] = series
        self.series_label = series_name
        self.add_running_mean_and_std()
        self.mean = series.mean()
        self.std = series.std()

    def add_running_mean_and_std(self):
        mean_name = self.series_label + "_running_mean"
        std_name = self.series_label + "_running_std"
        plus_std = self.series_label + "_plus_std"
        minus_std = self.series_label + "_minus_std"
        count = 1.0
        sum = 0
        self.df[mean_name] = pd.Series()
        self.df[std_name] = pd.Series()
        self.df[plus_std] = pd.Series()
        self.df[minus_std] = pd.Series()
        for i in range(len(self.df.index)):
            sum += self.df[self.series_label].iloc[i]
            self.df[mean_name].iat[i] = sum / count
            self.df[std_name].iat[i] = self.df[self.series_label][:i].std() / count
            self.df[plus_std].iat[i] = self.df[self.series_label].iloc[i] + self.df[self.series_label][:i].std()
            self.df[minus_std].iat[i] = self.df[self.series_label].iloc[i] - self.df[self.series_label][:i].std()
            count += 1