from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta


class SampleStrategy(IStrategy):
    INTERFACE_VERSION = 3
    timeframe = "5m"

    minimal_roi = {
        "0": 0.01
    }
    stoploss = -0.10

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["rsi"] = ta.RSI(dataframe)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["rsi"] < 70),
            "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[
            (dataframe["rsi"] > 95),
            "exit_long"] = 1
        return dataframe
