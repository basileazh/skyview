# for import config file
import os

import pandas
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
    :return: dict. ex : {'stock': px}
    """
    # Load tickers data, to get types and make a split
    tickers_df = pd.read_csv(f"{DIR}/{parameters['path_to_tickers_data']}", sep=";")
    unique_df_types = tickers_df["type"].unique()
    plots_df = {}
    for ticker_type in unique_df_types:
        print(f"Making df for plot for type {ticker_type}")
        type_ticker_cols = tickers_df.loc[
            tickers_df["type"] == ticker_type, "ticker"
        ].unique()
        print(f"{type_ticker_cols = }")
        # Melt to 3 columns : Date, ticker, value
        plots_df[ticker_type] = _melt_df_for_plotly(
            filter_df_columns_tickers(df, type_ticker_cols)
        )
        # Resample as in data_processing pipeline config
        plots_df[ticker_type] = _resample_plotly_df(
            plots_df[ticker_type], parameters["time_freq"]
        )
    return plots_df


def _resample_plotly_df(df: pd.DataFrame, freq: str = "w-MON") -> pd.DataFrame:
    """
    Resample a plotly-ready dataset, with 3 columns :
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
        .groupby("ticker")
        .resample(freq)
        .agg({"value": "sum"})
        .reset_index()
    )

    return df


def _melt_df_for_plotly(df: pd.DataFrame) -> pandas.DataFrame:
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
