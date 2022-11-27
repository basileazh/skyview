# for import config file
import os
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd

from skyview.modules.utils.utils import filter_df_columns_tickers

DIR = os.path.dirname(__file__)


def visualize_time_series_lines_by_type(df: pd.DataFrame, parameters) -> dict:
    """
    Creates a line plot with all columns in df
    One line plot is created by type of ticker, as described in
    src/skyview/modules/data_visualization/tickers_data.csv
    :param df: df to plot
    :param parameters: In conf/base/catalog:
    Defaults to {"figsize": (30, 20)}
    :return: dict. ex : {'stock': plt}
    """
    # Load tickers data, to get types and make a split
    tickers_df = pd.read_csv(f"{DIR}/{parameters['path_to_tickers_data']}", sep=";")
    unique_df_types = tickers_df["type"].unique()
    plots = {}
    for ticker_type in unique_df_types:
        print(f"Making plot for type {ticker_type}")
        type_ticker_cols = tickers_df.loc[
            tickers_df["type"] == ticker_type, "ticker"
        ].unique()
        print(f"{type_ticker_cols = }")
        plots[ticker_type] = _visualize_time_series_lines(
            filter_df_columns_tickers(df, type_ticker_cols), **parameters["plot"]
        )

    return plots


def _visualize_time_series_lines(
    df: pd.DataFrame, query: Union[str, None] = None, **kwargs
) -> plt:
    """
    Creates a line plot with all columns in df
    :param df: df to plot
    :param query: optional SQL query on the df
    :param kwargs: other args to pass to sns.set function
    Defaults to {"figsize": (30, 20)}
    :return: plt
    """
    if query:
        df = df.query(query)

    print(df)
    fig, ax = plt.subplots()
    for col in df.columns:
        print(f"{col = }")
        ax.plot(df.index, df[col])
    ax.legend(df.columns)

    return fig
