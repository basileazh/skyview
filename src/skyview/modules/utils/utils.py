import os
from datetime import datetime, timedelta
from re import sub

import pandas as pd

# ############# CONFIG ############# #
import yaml
from yaml.loader import SafeLoader

DIR = os.path.dirname(__file__)


def load_config() -> dict:
    """
    Loads the configuration for the projectf, in the ../config.yml
    :return: config
    """
    # Open the file and load the file
    with open(f"{DIR}/../config.yml") as f:
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
