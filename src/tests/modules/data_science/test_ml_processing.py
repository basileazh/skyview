import pandas as pd

from skyview.modules.data_science.ml_processing import format_ds_y_prophet


def test_format_ds_y_prophet():
    data = pd.DataFrame(
        {
            "Date": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "TSLA": [1, 2, 3],
            "GOOG": [4, 5, 6],
        }
    ).set_index("Date")
    expected = pd.DataFrame(
        {
            "ds": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "y": [1, 2, 3],
            "GOOG": [4, 5, 6],
        }
    )

    assert format_ds_y_prophet(data, "TSLA").equals(expected)
