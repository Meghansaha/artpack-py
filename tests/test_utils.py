###############################################################################
# _utils.py Test Suite
###############################################################################
import pytest
import re
import random
from unittest.mock import patch
from artpack._utils import _check_type
from artpack._utils import _is_valid_color
from artpack._utils import _is_positive_number

# =============================================================================#
# _check_type Tests
# =============================================================================#


def test_check_type_raises_with_mismatched_type():
    test_object = "A lil string"

    with pytest.raises(TypeError) as exc_info:
        _check_type("test_object", test_object, int)

    error_msg = str(exc_info.value)
    assert ("`test_object` should be of type `int`.\n") in error_msg
    assert ("You've supplied a `str` object") in error_msg


# =============================================================================#
# _is_valid_color Tests
# =============================================================================#
def test_is_valid_raises_on_wrong_type():
    bad_color_type = ["#000000"]

    with pytest.raises(TypeError) as exc_info:
        _is_valid_color("color_choice", bad_color_type)

    error_msg = str(exc_info.value)
    assert ("`color_choice` should be of type `str`") in error_msg
    assert ("You've supplied a `list` object") in error_msg


def test_is_valid_color_raises_on_invalid_color():
    bad_hex_color = "#e7223"

    with pytest.raises(ValueError) as exc_info:
        _is_valid_color("hex_color", bad_hex_color)

    error_msg = str(exc_info)
    assert "`hex_color` must be a valid hex color (#RRGGBB or #RGB)"
    assert "or a named matplotlib color. You've supplied: '#e7223'"


def test_is_valid_color_accepts_valid_matplotlib_color_name():
    color_choice = "purple"

    _is_valid_color("color_choice", color_choice)  # Should not raise


def test_is_valid_color_accepts_valid_hex_color():
    color_choice = "#1a1a1a"

    _is_valid_color("color_choice", color_choice)  # Should not raise


# =============================================================================#
# _is_positive_number Tests
# =============================================================================#


def test_is_positive_number_raises_on_negative_number():
    with pytest.raises(ValueError) as exc_info:
        _is_positive_number("max_number", -20)

    error_msg = str(exc_info)

    assert (
        "`max_number` must be a positive integer or float (number with decimals)."
    ) in error_msg
    assert ("You've supplied: `-20`") in error_msg
