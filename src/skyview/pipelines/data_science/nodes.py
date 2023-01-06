"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""

import pandas as pd

from skyview.modules.data_science.ml_processing import (
    format_ds_y_prophet
)


def format_ds_y_prophet_node(data: pd.DataFrame, parameters: dict) -> pd.DataFrame:
    """
    Format data for prophet
    Reset index Date into ds and renames y_name into y column
    :param data: pd.DataFrame
    :param parameters: dict
    :return: pd.DataFrame
    """

    return format_ds_y_prophet(data, parameters["y_name"], parameters["date_name"])  # return formatted data
