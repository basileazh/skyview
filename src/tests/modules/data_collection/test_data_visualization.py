"""
Pytest test framework
test file for src/skyview/modules/data_visualization/data_visualization.py
"""
import pandas as pd

from skyview.modules.data_visualization.data_visualization import (
    _filter_date_plotly_df,
    _filter_price_timing_plotly_df,
    _resample_plotly_df,
)


def test__resample_plotly_df():
    """
    Test for skyview.modules
            .data_visualization
            .data_visualization
            ._resample_plotly_df
            function
    Resample based on pandas-style freq a plotly-ready dataset
    :return:
    """
    # INPUTS
    input_df = pd.DataFrame(
        [
            [pd.to_datetime("2014-02-01"), "open__cac40", 99],
            [pd.to_datetime("2014-02-02"), "open__cac40", 99],
            [pd.to_datetime("2014-02-03"), "open__cac40", 99],
            [pd.to_datetime("2014-02-04"), "open__cac40", 99],
            [pd.to_datetime("2014-02-05"), "open__cac40", 99],
            [pd.to_datetime("2014-02-06"), "open__cac40", 99],
            [pd.to_datetime("2014-02-07"), "open__cac40", 99],
            [pd.to_datetime("2014-02-08"), "open__cac40", 99],
            [pd.to_datetime("2014-02-09"), "open__cac40", 99],
            [pd.to_datetime("2014-02-10"), "open__cac40", 99],
            [pd.to_datetime("2014-02-03"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-04"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-05"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-06"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-07"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-08"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-09"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-10"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-11"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-12"), "high__btc_usd", 99],
        ],
        columns=["Date", "ticker", "value"],
    )

    freq = "W-MON"

    # OUTPUT
    output_df = pd.DataFrame(
        [
            [pd.to_datetime("2014-02-03"), "high__btc_usd", 99],
            [pd.to_datetime("2014-02-10"), "high__btc_usd", 693],
            [pd.to_datetime("2014-02-17"), "high__btc_usd", 198],
            [pd.to_datetime("2014-02-03"), "open__cac40", 297],
            [pd.to_datetime("2014-02-10"), "open__cac40", 693],
        ],
        columns=["Date", "ticker", "value"],
    )

    result_df = _resample_plotly_df(input_df, freq=freq).reset_index(drop=True)
    # print(f"{result_df = }")
    assert result_df.equals(output_df)


def test__filter_date_plotly_df():
    """
    Test for skyview.modules
            .data_visualization
            .data_visualization
            ._filter_date_plotly_df
            function
    Filters a plotly_ready dataset
    between start_date_plot and end_date_plot
    :return:
    """
    # INPUTS
    input_df = pd.DataFrame(
        [
            [pd.to_datetime("2014-02-09"), "open__cac40", 99],
            [pd.to_datetime("2021-01-01"), "high__btc_usd", 100],
            [pd.to_datetime("2022-04-05"), "close__amzn", 101],
            [pd.to_datetime("2022-08-16"), "volume__goog", 102],
        ],
        columns=["Date", "ticker", "value"],
    )

    start_date_plot = "2020-01-01"
    end_date_plot = "2022-01-01"

    # OUTPUT
    output_df = pd.DataFrame(
        [
            [pd.to_datetime("2021-01-01"), "high__btc_usd", 100],
        ],
        columns=["Date", "ticker", "value"],
    )

    result_df = _filter_date_plotly_df(
        input_df, start_date_plot=start_date_plot, end_date_plot=end_date_plot
    ).reset_index(drop=True)

    assert result_df.equals(output_df)


def test__filter_price_timing_plotly_df():
    """
    Test for skyview.modules
            .data_visualization
            .data_visualization
            ._filter_price_timing_plotly_df
            function
    Filters tickers based on price timing criteria
    Timing values : close, open, high, low
    :return:
    """
    # INPUTS
    input_df = pd.DataFrame(
        [
            [pd.to_datetime("2014-02-09"), "open__cac40", 99],
            [pd.to_datetime("2021-01-01"), "high__btc_usd", 100],
            [pd.to_datetime("2022-04-05"), "close__amzn", 101],
            [pd.to_datetime("2022-08-16"), "volume__goog", 102],
        ],
        columns=["Date", "ticker", "value"],
    )

    price_timings = ["close", "volume"]

    # OUTPUT
    output_df = pd.DataFrame(
        [
            [pd.to_datetime("2022-04-05"), "close__amzn", 101],
            [pd.to_datetime("2022-08-16"), "volume__goog", 102],
        ],
        columns=["Date", "ticker", "value"],
    )

    result_df = _filter_price_timing_plotly_df(
        input_df, price_timings=price_timings
    ).reset_index(drop=True)

    assert result_df.equals(output_df)
