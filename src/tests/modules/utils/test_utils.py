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
    STRING = "Basile. El-_ &AzHArI/"
    assert snake_case(STRING) == "basile__el____az_h_ar_i/"
