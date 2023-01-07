"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    format_ds_y_prophet_node,
    compute_correlation_node,
)


def create_pipeline(**kwargs) -> Pipeline:

    pipeline_training = pipeline(
        [
            node(
                func=format_ds_y_prophet_node,
                inputs=["tickers_ts", "params:ml_processing"],
                outputs="input_prophet",
                name="format_ds_y_prophet_node",
                tags=["training"]
            ),

            # ####### 08 REPORTING ######## #


            # Tickers daily prices
            node(
                func=compute_correlation_node,
                inputs=["input_prophet"],
                outputs="correlation_input_model",
                name="compute_correlation_node",
                tags=["reporting"],
            ),
        ],
    )

    return pipeline(
        pipe=pipeline_training,  # + pipeline_evaluation + pipeline_inference),
        inputs={"tickers_ts"},
        parameters={
            "params:ml_processing",
        },
        namespace="data_science",
    )
