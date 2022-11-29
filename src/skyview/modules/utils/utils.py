import os
from datetime import datetime, timedelta
from re import sub

import pandas as pd

# ############# CONFIG ############# #
import yaml
from yaml.loader import SafeLoader

DIR = os.path.dirname(__file__)


def load_config(path=f"{DIR}/../config.yml") -> dict:
    """
    Loads the configuration for the projectf, in the ../config.yml
    :return: config
    """
    # Open the file and load the file
    with open(path) as f:
        config = yaml.load(f, Loader=SafeLoader)

    return config


config = load_config()


# ############# STR ############# #


def snake_case(s: str) -> str:
    """
    Transforms an inputed str to snake_case
    :param s: input str
    :return: snaked_case version of input str
    """
    return (
        "_".join(
            sub(
                "([A-Z][a-z]+)", r" \1", sub("([A-Z]+)", r" \1", s.replace("-", " "))
            ).split()
        )
        .lower()
        .replace("&", "")
        .replace(".", "_")
    )


def str_match_sub_in_str_list(super_str: str, str_list) -> bool:
    """
    Assesses if a super_str has a sub string in a list of strings
    :param super_str: super_string
    :param str_list: list of strings that would be sub strings of super_str
    :return: True/False
    """
    for str_ in str_list:
        if str_ in super_str:
            return True

    return False


# ############# LIST ############# #


def unique(list1):
    """
    Only keeps unique values in a list
    :param list1: list to remove redundentes
    :return: unique items list
    """
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)

    return unique_list


# ############# TICKERS ############# #


def filter_df_columns_tickers(df: pd.DataFrame, tickers_list_filter=["GOOG"]):
    """
    Filters a pd.DataFrame of tickers time series in columns
    to only keep tickers in tickers_list_filter.
    snake_case is applied to tockers to match cols format
    :param df: df to filter columns to a list of tickers
    :param tickers_list_filter: list of tickers to keed in df
    :return: df filtered by columns
    """

    tickers_list_snake_case = list(map(snake_case, tickers_list_filter))
    columns = df.columns.tolist()
    cols_to_keep = [
        col
        for col in columns
        if str_match_sub_in_str_list(col, tickers_list_snake_case)
    ]
    df_filtered = df[cols_to_keep]

    return df_filtered


# USELESS
def date_range(date_start: str, date_end: str, is_cut: bool = True) -> pd.DataFrame:
    """
    Returns a date 1 day less from the one inserted
    :param date_start: date_star for date range
    :param date_end: date_en for date range
    kwargs are arguments for datetime.timedelta
    :param is_cut: whether to include (True)
    the end_date day or to end 1 day less (False)
    :return: string 1 day less
    """
    if is_cut:
        delta = timedelta(days=-1)
        date_end_d = datetime.strptime(date_end, config["F"])
        date_end_d = date_end_d + delta
        date_end = date_end_d.strftime(config["F"])

    dr = pd.DataFrame(pd.date_range(date_start, date_end))

    return dr
