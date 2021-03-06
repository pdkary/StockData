from ta import *
from constants import TiingoKeys
import pandas as pd


class HasStockIndicators:

    def __init__(self, dataframe, name):
        self.name = name
        if type(dataframe) is str:
            self.df = pd.read_csv(dataframe).fillna(value=0)
        if type(dataframe) is pd.DataFrame:
            self.df = dataframe
            self.getIndicators()

    def getVolumeIdicators(self):
        self.ADI = acc_dist_index(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.CMF = chaikin_money_flow(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.EOM = ease_of_movement(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.FI = force_index(
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.NVI = negative_volume_index(
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.OBV = on_balance_volume(
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

        self.VPT = volume_price_trend(
            self.df[TiingoKeys.CLOSE.value],
            self.df[TiingoKeys.VOLUME.value], fillna=True)

    def getVolatilityIndicators(self):
        self.ATR = average_true_range(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.BBH = bollinger_hband(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.BBHI = bollinger_hband_indicator(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.BBL = bollinger_lband(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.BBLI = bollinger_hband_indicator(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.BBMA = bollinger_mavg(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.DCHB = donchian_channel_hband(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.DCHBI = donchian_channel_hband_indicator(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.DCLB = donchian_channel_lband(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.DCLBI = donchian_channel_lband_indicator(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KC = keltner_channel_central(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KCHB = keltner_channel_hband(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KCHBI = keltner_channel_hband_indicator(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KCLB = keltner_channel_lband(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KCLBI = keltner_channel_lband_indicator(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

    def getTrendIndicators(self):
        self.ADX = adx(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.ADXN = adx_neg(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.ADXP = adx_pos(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.AID = aroon_down(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.AIU = aroon_up(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.CCI = cci(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.DPO = dpo(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.EMA = ema_indicator(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.ICHIA = ichimoku_a(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value], fillna=True)

        self.ICHIB = ichimoku_b(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value], fillna=True)

        self.KST = kst(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.KSTSIG = kst_sig(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.MACD = macd(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.MACDDIF = macd_diff(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.MACDSIG = macd_signal(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.MI = mass_index(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value], fillna=True)

        self.TRIX = trix(
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.VORTEXN = vortex_indicator_neg(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

        self.VORTEXP = vortex_indicator_pos(
            self.df[TiingoKeys.HIGH.value],
            self.df[TiingoKeys.LOW.value],
            self.df[TiingoKeys.CLOSE.value], fillna=True)

    def getIndicators(self):
        self.getVolatilityIndicators()
        self.getTrendIndicators()
