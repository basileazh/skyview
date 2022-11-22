"""
A module to get financial data from API.

Methods
-------
yf_retrieve : Retrieve tickers daily historic prices from yahoo yfinance API
"""

from datetime import datetime

import pandas as pd
import yfinance as yf

# Config
from ..utils.utils import load_config, snake_case

config = load_config()


def yf_retrieve(
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
    data = pd.DataFrame(data).reset_index()

    return data


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Flatten columns levels by joining with "_"
    - Converts all columns to snake case
    :param df: df with columns names to be cleaned
    :return: DataFrame with cleaned columns
    """
    df.columns = [snake_case("_".join(col)) for col in df.columns.values]
    df.rename({"date_": "date"}, axis=1, inplace=True)

    return df
