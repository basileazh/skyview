"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

import pandas as pd

from skyview.modules.data_collection.data_collection import clean_columns, yf_retrieve
from skyview.modules.data_visualization.data_visualization import (
    visualize_time_series_lines_by_type,
)


def yf_retrieve_node(e: Any, parameters: Any):
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


def clean_df_node(df: pd.DataFrame) -> pd.DataFrame:
    """
    - Flatten columns levels by joining with "_"
    - Converts all columns to snake case
    :param df: df with columns names to be cleaned
    :return: DataFrame with cleaned columns
    """
    df = clean_columns(df)

    return df


def visualize_time_series_lines_by_type_node(data: pd.DataFrame, parameters: Any):
    """
    Creates a line plot with all columns in data
    One line plot is created by type of ticker, as described in
    src/skyview/modules/data_visualization/tickers_data.csv
    :param data: data to plot
    :param parameters: In conf/base/catalog:
    Defaults to {"figsize": (30, 20)}
    :return: plt
    """
    plots = visualize_time_series_lines_by_type(data, parameters)
    print(plots)
    return (
        plots["index"],
        plots["stock"],
        plots["commodity"],
        plots["crypto"],
    )
