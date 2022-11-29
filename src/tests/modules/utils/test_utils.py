"""
Pytest test framework
test file for src/skyview/modules/utils/utils.py
"""

from skyview.modules.utils.utils import snake_case


def test_snake_case():
    """
    Test for skyview.modules.utils.utils.snake_case function
    Transforms an inputed str to snake_case
    """
    input_str = "Basile. El-_ &AzHArI/"
    output_str = "basile__el____az_h_ar_i/"
    assert snake_case(input_str) == output_str
