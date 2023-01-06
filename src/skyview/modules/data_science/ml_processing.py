import pandas as pd


def format_ds_y_prophet(data: pd.DataFrame, y_name: str, date_name: str = "Date") -> pd.DataFrame:
    """
    Format data for prophet
    Reset index Date into ds and renames y_name into y column
    :param data: pd.DataFrame
    :param y_name: str
    :param date_name: str
    :return: pd.DataFrame
    """
    return data.reset_index().rename(columns={date_name: "ds", y_name: "y"})  # return formatted data


if __name__ == "__main__":
    data = pd.DataFrame(
        {
            "Date": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "TSLA": [1, 2, 3],
            "GOOG": [4, 5, 6],
        }
    )

    print(format_ds_y_prophet(data, "TSLA").columns)
