"""Internal utility functions for artpack."""

import re
from typing import Any
from matplotlib import colors as mcolors

###############################################################################
# Type validation
###############################################################################


def _check_type(param: Any, expected_type: str) -> bool:
    """Internal type checker for dev

    Parameters
    ----------
    param : Any, required
        Object to check the type of
    expected_type : str, required
        A string value of the expected type to check `param` for.

    Returns
    -------
    bool
        Returns True if `param` matches the `expected_type`. Otherwise, will return False.
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


###############################################################################
# Color validation
###############################################################################


def is_valid_color(color: str) -> bool:
    """
    Check if a string is a valid color specification.

    Accepts hex colors (#RRGGBB or #RGB) and named matplotlib colors.

    Parameters
    ----------
    color : str
        Color string to validate

    Returns
    -------
    bool
        True if valid color, False otherwise
    """
    if not isinstance(color, str):
        type_input = type(color)

        raise TypeError(f"color should be of  string")
        return False

    # Check if it's a valid hex color (6 or 3 digits)
    hex_pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"
    if re.match(hex_pattern, color):
        return True

    # Check if it's a named matplotlib color
    if color.lower() in mcolors.CSS4_COLORS:
        return True

    return False


def validate_color(color: str, param_name: str = "color") -> None:
    """
    Validate a color parameter and raise ValueError if invalid.

    Parameters
    ----------
    color : str
        Color string to validate
    param_name : str, default "color"
        Name of the parameter for error messages

    Raises
    ------
    ValueError
        If color is not valid
    """
    if not is_valid_color(color):
        raise ValueError(
            f"{param_name} must be a valid hex color (#RRGGBB or #RGB) "
            f"or named matplotlib color. You've supplied: {color}"
        )


###############################################################################
# Positive Numeric Values
###############################################################################
"""
Check if a string is a valid color specification.

Accepts hex colors (#RRGGBB or #RGB) and named matplotlib colors.

Parameters
----------
number : str
    Color string to validate

Returns
-------
bool
    True if valid color, False otherwise
"""


def is_positive_number(number: float | int) -> bool:
    if not isinstance(number, (int, float)) or number <= 0:
        raise ValueError(
            f"number must be a positive integer or float (number with decimals). You've supplied: {number}"
        )

    return True
