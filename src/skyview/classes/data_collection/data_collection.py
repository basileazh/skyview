from datetime import datetime

import pandas as pd
import yfinance as yf

# Config
from ..utils.utils import load_config

config = load_config()


class YfinanceCollection:
    """
    A class to get financial data from yfinance API.

    Methods
    -------
    retrieve (static) : Retrieve tickers daily historic prices from yahoo yfinance API
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def retrieve(
        ticker_list: list = ["GOOG"],
        start_date: str = "2015-01-01",
        end_date: str = datetime.today().strftime(config["F"]),
    ) -> pd.DataFrame:
        """
        Retrieve tickers daily historic prices from yahoo yfinance API

        :param start_date: start date to get tickers data
        :param end_date: end date to get tickers history prices
        :param ticker_list: list of tickers to retrieve. ex : GOOG, AAPL, TSLA, BTC-USD
        Full tickers available at https://finance.yahoo.com/lookup

        :return: tickers daily historic prices
        """
        end_date = str(end_date)

        # Pull close data from Yahoo Finance for the list of tickers
        data = yf.download(ticker_list, start=start_date, end=end_date)
        data = pd.DataFrame(data)

        return data
