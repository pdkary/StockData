import pandas as pd


class EnhancedSeries:

    def __init__(self, name, series):
        self.df = pd.DataFrame(index=series.index)
        self.series_label = name
        self.series = series
        self.mean = series.mean()
        self.std = series.std()

        self.mean_name = name + "_running_mean"
        self.std_name = name + "_running_std"
        self.plus_std = name + "_plus_std"
        self.minus_std = name + "_minus_std"
        # self.above_sigma = name + "_above_sigma"

        self.analyze()
        self.df.fillna()
        for x in self.df.columns:
            print(x)

    def analyze(self):
        count = 0
        total = 0
        sigma = 3
        mean_series = pd.Series().astype("float")
        std_series = pd.Series().astype("float")
        plus_std_series = pd.Series().astype("float")
        minus_std_series = pd.Series().astype("float")
        # above_sigma_series = pd.Series()
        for i, stamp in enumerate(self.series.index):
            count += 1
            value = self.series.iloc[i]
            std = self.series[:i].std()
            mean = total / count
            total += value
            plusStd = value + sigma * std
            minusStd = value - sigma * std
            mean_series.at[stamp] = mean
            std_series.at[stamp] = std
            plus_std_series.at[stamp] = plusStd
            minus_std_series.at[stamp] = minusStd
            # above_sigma_series.at[stamp] = 1 if value > plusStd or value < minusStd else 0
            count += 1

        self.df[self.mean_name] = mean_series
        self.df[self.std_name] = std_series
        self.df[self.plus_std] = plus_std_series
        self.df[self.minus_std] = minus_std_series
        # self.df[self.above_sigma] = above_sigma_series
