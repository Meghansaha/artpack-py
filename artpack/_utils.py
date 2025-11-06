"""Internal utility functions for artpack."""

import re
from typing import Any
from matplotlib import colors as mcolors

###############################################################################
# Type validation
###############################################################################


def _check_type(param_name: str, param: Any, expected_type: str) -> bool:
    """
    Internal type checker for dev. Raises if invalid.

    Parameters
    ----------
    param_name : str, required
        Name of the parameter to be checked in the parent function.
    param : Any, required
        Object to check the type of
    expected_type : str, required
        A string value of the expected type to check `param` for.

    Raises
    ------
    ValueError
        If type of `param` does not match the `expected_type` value.

    Returns
    -------
    bool
        Returns True if `param` matches the `expected_type`. Otherwise, will raise.
    """

    dict_types = (
        "int",
        "float",
        "complex",
        "bool",
        "str",
        "tuple",
        "list",
        "polars.dataframe.frame.DataFrame",
        "pandas.core.frame.DataFrame",
    )

    if expected_type not in dict_types:
        raise ValueError(
            f"expected_type most be one of: {', '.join(dict_types)}. "
            f"You've supplied: {expected_type}"
        )


# PICK UP HERE. Add type check and finish doc string cleanup for others.


###############################################################################
# Color validation
###############################################################################


def _is_valid_color(param_name: str, color: str):
    """
    Internal check to validate color string (hex or matplotlib named). Raises if invalid.

    Parameters
    ----------
    param_name : str
        Name of the color parameter to be checked in the parent function

    color : str
        Color string to validate

    Raises
    ------
    ValueError
        If color is not a valid hexadecimal webcolor or a named matplotlib color.

    """
    if not isinstance(color, str):
        type_input = type(color)

        raise TypeError(
            f"{param_name} should be a string. " f"You've supplied a {type_input}"
        )

    # Check if it's a valid hex color (6 or 3 digits)
    hex_color = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    invalid_hex_color = not re.match(hex_color, color)

    # Check if it's a named matplotlib color
    invalid_matplotlib_color = color.lower() not in mcolors.CSS4_COLORS

    if invalid_hex_color and invalid_matplotlib_color:
        raise ValueError(
            f"{param_name} must be a valid hex color (#RRGGBB or #RGB) "
            f"or named matplotlib color. You've supplied: {color}"
        )


###############################################################################
# Positive Numeric Values
###############################################################################
"""
Internal validator for positive int/float values. Raises on invalid.

Parameters
----------
param_name: str
    Name of the number parameter to be checked in the parent function.
number : float, int
    Number to check

Raises
------
ValueError
    If number is not a positive float or integer.

Returns
-------
bool
    True if valid positive int or float
"""


def is_positive_number(param_name: str, number: float | int) -> bool:
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError(
            f"{param_name} must be a positive integer or float (number with decimals). You've supplied: {number}"
        )

    return True
