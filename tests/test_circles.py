###############################################################################
# circles.py Test Suite
###############################################################################
import pytest
import re
import random
from unittest.mock import patch
from artpack import art_pals
from artpack.palettes import pals


# Input validations
## Numeric type checks
circle_data_error_cases = [
    {
        "id": "x is not a number",
        "kwargs": {"x": "-4", "y": 8, "radius": 5},
        "error_msg": "`x` should be of type `",
    }
]
