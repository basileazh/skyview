"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
from typing import Any

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import clean_df_node, visualize_time_series_by_type_node, yf_retrieve_node


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
                tags=["etl"],
            ),
            # ###### 02 INTERMEDIATE ###### #
            # Tickers daily prices
            node(
                func=clean_df_node,
                inputs="raw_tickers_ts",
                outputs=["tickers_ts", "tickers_ts_reporting"],
                name="clean_df_node",
                tags=["etl"],
            ),
            # ####### 08 REPORTING ######## #
            # Tickers daily prices
            node(
                func=visualize_time_series_by_type_node,
                inputs=["tickers_ts_reporting", "params:visualize_time_series"],
                outputs=[
                    "reporting_tickers_ts_lines_index_price",
                    "reporting_tickers_ts_lines_index_volume",
                    "reporting_tickers_ts_lines_stock_price",
                    "reporting_tickers_ts_lines_stock_volume",
                    "reporting_tickers_ts_lines_commodity_price",
                    "reporting_tickers_ts_lines_commodity_volume",
                    "reporting_tickers_ts_lines_crypto_price",
                    "reporting_tickers_ts_lines_crypto_volume",
                ],
                name="visualize_time_series_lines_by_type_node",
                tags=["reporting"],
            ),
        ],
        parameters={"params:yf_retrieve", "params:visualize_time_series"},
        inputs="empty_input",
        namespace="data_processing",
        outputs={
            "tickers_ts",
            "reporting_tickers_ts_lines_index_price",
            "reporting_tickers_ts_lines_index_volume",
            "reporting_tickers_ts_lines_stock_price",
            "reporting_tickers_ts_lines_stock_volume",
            "reporting_tickers_ts_lines_commodity_price",
            "reporting_tickers_ts_lines_commodity_volume",
            "reporting_tickers_ts_lines_crypto_price",
            "reporting_tickers_ts_lines_crypto_volume",
        },
    )
