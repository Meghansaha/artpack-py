###############################################################################
# circles.py Test Suite
###############################################################################
import pytest
import re
import random
from unittest.mock import patch
from artpack import circle_data


# Input validations
## Numeric type checks
circle_data_numeric_error_cases = [
    {
        "id": "x is not a number",
        "kwargs": {"x": "-4", "y": 8, "radius": 5},
        "exc": TypeError,
        "error_msg": "`x` should be of type `float` or `int`.\nYou've supplied a `str` object",
    },
    {
        "id": "y is not a number",
        "kwargs": {"x": -4, "y": int, "radius": 5},
        "exc": TypeError,
        "error_msg": "`y` should be of type `float` or `int`.\nYou've supplied a `type` object",
    },
    {
        "id": "radius is not a number",
        "kwargs": {"x": -4, "y": 5, "radius": "Big boi"},
        "exc": TypeError,
        "error_msg": "`radius` should be of type `float` or `int`.\nYou've supplied a `str` object",
    },
    {
        "id": "n_points is not an int",
        "kwargs": {"x": -4, "y": 5, "radius": 10, "n_points": 100.2},
        "exc": TypeError,
        "error_msg": "`n_points` should be of type `int`.\nYou've supplied a `float` object",
    },
    {
        "id": "radius is not positive",
        "kwargs": {"x": -4, "y": 5, "radius": -8},
        "exc": ValueError,
        "error_msg": "`radius` must be a positive integer or float (number with decimals).\nYou've supplied: `-8`",
    },
    {
        "id": "n_points is not gte 100",
        "kwargs": {"x": -4, "y": 5, "radius": 10, "n_points": 99},
        "exc": ValueError,
        "error_msg": "`n_points` must be >= 100 for a reasonable approximation of a circle.\nYou've supplied: `99`",
    },
]


@pytest.mark.parametrize(
    "case",
    circle_data_numeric_error_cases,
    ids=[case["id"] for case in circle_data_numeric_error_cases],
)
def test_numeric_error_messages(case):
    with pytest.raises(case["exc"], match=re.escape(case["error_msg"])):
        circle_data(**case["kwargs"])


## String type checks
circle_data_string_error_cases = [
    {
        "id": "Color is invalid",
        "kwargs": {"x": -4, "y": 5, "radius": 10, "color": "A Cool Blue"},
        "exc": ValueError,
        "error_msg": "`color` must be a valid hex color (#RRGGBB or #RGB) or a named matplotlib color.\nYou've supplied: 'A Cool Blue'",
    },
    {
        "id": "Fill is invalid",
        "kwargs": {"x": -4, "y": 5, "radius": 10, "fill": "The VOID"},
        "exc": ValueError,
        "error_msg": "`fill` must be a valid hex color (#RRGGBB or #RGB) or a named matplotlib color.\nYou've supplied: 'The VOID'",
    },
    {
        "id": "group_value is missing when group_var == True",
        "kwargs": {
            "x": -4,
            "y": 5,
            "radius": 10,
            "group_var": True,
            "group_value": None,
        },
        "exc": TypeError,
        "error_msg": "`group_value` should be of type `str`.\nYou've supplied a `NoneType` object",
    },
]


@pytest.mark.parametrize(
    "case",
    circle_data_string_error_cases,
    ids=[case["id"] for case in circle_data_string_error_cases],
)
def test_string_error_messages(case):
    with pytest.raises(case["exc"], match=re.escape(case["error_msg"])):
        circle_data(**case["kwargs"])
