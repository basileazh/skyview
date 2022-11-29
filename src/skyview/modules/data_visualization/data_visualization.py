# for import config file
import os
from datetime import datetime

import pandas as pd

# Config
from skyview.modules.utils.utils import filter_df_columns_tickers, load_config

config = load_config()
DIR = os.path.dirname(__file__)


def visualize_time_series_by_type(df: pd.DataFrame, parameters) -> dict:
    """
    Creates a plot with all columns in df
    One plot is created by type of ticker, as described in
    src/skyview/modules/data_visualization/tickers_data.csv,
    and volume is plotted separate from prices
    :param df: df to plot
    :param parameters: In conf/base/catalog:
    Defaults to {"figsize": (30, 20)}
    :return: dict. ex : {'stock': px}
    """
    # Load tickers data, to get types and make a split
    tickers_df = pd.read_csv(f"{DIR}/{parameters['path_to_tickers_data']}", sep=";")
    unique_df_types = tickers_df["type"].unique()
    plots_df = {}
    for ticker_type in unique_df_types:
        # Filter on columns who belong to ticker_type
        print(f"Making df for plot for type {ticker_type}")
        type_ticker_cols = tickers_df.loc[
            tickers_df["type"] == ticker_type, "ticker"
        ].unique()
        print(f"{type_ticker_cols = }")

        # Melt to 3 columns : Date, ticker, value
        df_plot = _melt_df_for_plotly(filter_df_columns_tickers(df, type_ticker_cols))

        # Resample as in data_processing pipeline config
        df_plot = _resample_plotly_df(df_plot, parameters["time_freq"])

        # Filter data between start_date_plot and end_date_plot
        df_plot = _filter_date_plotly_df(
            df_plot, parameters["start_date_plot"], parameters["end_date_plot"]
        )

        # Filter price timings as inputed in price_timing parameter
        # between close, open, high, low
        df_plot = _filter_price_timing_plotly_df(df_plot, parameters["price_timing"])

        # Separate proces and volume
        plots_df[f"{ticker_type}_price"] = df_plot.loc[
            ~df_plot["ticker"].str.startswith(parameters["volume_columns_str"])
        ]
        plots_df[f"{ticker_type}_volume"] = df_plot.loc[
            df_plot["ticker"].str.startswith(parameters["volume_columns_str"])
        ]
    return plots_df


def _melt_df_for_plotly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a dataframe with only 3 columns :
    Date, ticker, value
    Input dataframe should have Date as index,
    time series as columns
    :param df: df to plot
    :return: pd.DataFrame
    """
    # Melt data frame to obtain only 3 columns :
    # Date, ticker, value
    df = df.reset_index().melt(id_vars=["Date"], var_name="ticker", value_name="value")

    return df


def _resample_plotly_df(df: pd.DataFrame, freq: str = "w-MON") -> pd.DataFrame:
    """
    Resample based on pandas-style freq a plotly-ready dataset, with 3 columns :
    Date, ticker, value
    This df is outputed by _melt_df_for_plotly
    Args:
        df: plotly-ready df to resample
        freq: time frequency, default to weekly starting on monday

    Returns: pd.DataFrame plotly-ready and resampled

    """
    # Resampling data on inputed time frequency
    df = (
        df.set_index("Date")
        .groupby(["ticker"])
        .resample(freq)
        .agg({"value": "sum"})
        .reset_index()
    )
    df = df[["Date", "ticker", "value"]]

    return df


def _filter_date_plotly_df(
    df: pd.DataFrame, start_date_plot: str = "2018-01-01", end_date_plot: str = "today"
):
    """
    Filters a plotly_ready dataset
    between start_date_plot and end_date_plot
    This df is outputed by _melt_df_for_plotly
    Args:
        df: plotly-ready dataset to be filtered
        start_date_plot: lower time bound, included
        Defaults at "2018-01-01"
        end_date_plot: upper time bound, included
        If "today" is given, current date is used

    Returns: filtered plotly-ready dataset

    """
    if end_date_plot == "today":
        end_date_plot = str(datetime.today().strftime(config["F"]))

    start_date_plot = pd.to_datetime(start_date_plot)
    end_date_plot = pd.to_datetime(end_date_plot)

    df = df.loc[(df["Date"] >= start_date_plot) & (df["Date"] <= end_date_plot)]

    return df


def _filter_price_timing_plotly_df(
    df: pd.DataFrame, price_timings: list = ["close", "volume"]
) -> pd.DataFrame:
    """
    Filters tickers based on price timing criteria
    Timing values : close, open, high, low
    Args:
        df: df to filter by price timing
        price_timings: list in lose, open, high, low

    Returns: pd.DataFrame filtered on price type

    """
    # List of tickers in price_timings
    tickers_list = []
    for price_timing in price_timings:
        tickers_list.extend([t for t in df["ticker"] if t.startswith(price_timing)])

    df = df.loc[df["ticker"].isin(tickers_list)]

    return df


# def _visualize_time_series_lines_matplotlib(
#     df: pd.DataFrame, query: Union[str, None] = None, **kwargs
# ) -> plt:
#     """
#     Creates a line plot with all columns in df
#     :param df: df to plot
#     :param query: optional SQL query on the df
#     :param kwargs: other args to pass to sns.set function
#     Defaults to {"figsize": (30, 20)}
#     :return: plt
#     """
#     if query:
#         df = df.query(query)
#
#     fig, ax = plt.subplots()
#     for col in df.columns:
#         print(f"{col = }")
#         ax.plot(df.index, df[col])
#     ax.legend(df.columns)
#
#     return fig
