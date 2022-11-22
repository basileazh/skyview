"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_df_node, yf_retrieve_node


def create_pipeline(**kwargs: Any) -> Pipeline:
    return pipeline(
        [
            # ########## 01 RAW ########## #
            # Tickers daily prices
            node(
                func=yf_retrieve_node,
                inputs=["empty_input", "params:yf_retrieve"],
                outputs=["raw_tickers_ts", "raw_tickers_ts_csv"],
                name="yf_retrieve_node",
            ),
            # ###### 02 INTERMEDIATE ###### #
            # Tickers daily prices
            node(
                func=clean_df_node,
                inputs="raw_tickers_ts",
                outputs="inter_tickers_ts",
                name="clean_df_node",
            ),
        ],
        parameters="params:yf_retrieve",
        inputs="empty_input",
        namespace="data_processing",
        # outputs={"tickers_ts", "tickers_ts_csv"},
        outputs="inter_tickers_ts",
    )
