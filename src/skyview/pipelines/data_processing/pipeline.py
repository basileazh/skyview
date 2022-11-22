"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import yf_retrieve_node


def create_pipeline(**kwargs: Any) -> Pipeline:
    return pipeline(
        [
            # 01 RAW to 02 INTERMEDIATE Tickers daily closing prices
            node(
                func=yf_retrieve_node,
                inputs=["empty_input", "params:yf_retrieve"],
                outputs=["tickers_ts", "tickers_ts_csv"],
                name="yf_retrieve_node",
            ),
        ],
        parameters="params:yf_retrieve",
        inputs="empty_input",
        namespace="data_processing",
        outputs={"tickers_ts", "tickers_ts_csv"},
    )
