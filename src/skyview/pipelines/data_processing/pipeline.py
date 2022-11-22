"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import retrieve_yfinance_closing


def create_pipeline(**kwargs: Any) -> Pipeline:
    return pipeline(
        [
            # 01 RAW to 02 INTERMEDIATE Tickers daily closing prices
            node(
                func=retrieve_yfinance_closing,
                inputs=["empty_input", "params:retrieve_yfinance_closing"],
                outputs=["tickers_closing", "tickers_closing_csv"],
                name="retrieve_yfinance_closing",
            ),
        ],
        parameters="params:retrieve_yfinance_closing",
        inputs="empty_input",
        namespace="data_processing",
        outputs="tickers_closing",
    )
