"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

import pandas as pd

from ...modules.data_collection.data_collection import yf_retrieve


def yf_retrieve_node(e: Any, parameters: Any) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Retrieve tickers daily historic prices from yahoo yfinance API
        :param e: /
        :param parameters:
        In conf/base/catalog:
            :param activate: bool to run the code in the node
            :param start_date: start date to get tickers data
            :param end_date: end date to get tickers history prices
            :param ticker_list: list of tickers to retrieve. ex : GOOG, TSLA, BTC-USD
            Full tickers available at https://finance.yahoo.com/lookup

        :return: tickers daily historic prices
    """

    tickers_ts = yf_retrieve(
        parameters["tickers_list"],
        parameters["start_date"],
        parameters["end_date"],
    )

    return tickers_ts, tickers_ts
