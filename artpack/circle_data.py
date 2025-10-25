###############################################################################
# artpack/circle_data.py
###############################################################################
import random
from typing import List
import numpy as np
import polars as pl
from matplotlib import colors as mcolors


def circle_data(
    x: float,
    y: float,
    radius: float,
    color: str = None,
    fill: str = None,
    n_points: int = 100,
    group_var: bool = False,
    group_prefix: str = "circle_",
) -> pl.DataFrame:
    """
    Data Generation for Circles. A tool for creating a data frame of values that creates a circle with a specified radius
    when plotted. The `geom_path` and `geom_polygon` geoms are recommended with this data for use in `plotnine` for generative art.

    Parameters
    ----------
    x : float
        The center x-coordinate of the circle.
    y : float
        The center y-coordinate of the circle.
    radius : float
        The radius of the circle. Must be greater than 0.
    color : str, optional
        The outline color of the circle. Default None.
    fill : str, optional
        The fill color of the circle. Default None.
    n_points : int, default 100
        Number of points to generate along the circle's perimeter.
    group_var : bool, default False
        Whether to include a grouping variable in the output.
    group_prefix : str, default "circle_"
        Prefix for the grouping variable name.

    Returns
    -------
    pl.DataFrame
        A DataFrame containing the circle's coordinates with columns:
        - x: x-coordinates of points along the circle's perimeter
        - y: y-coordinates of points along the circle's perimeter
        - color: outline color (if specified)
        - fill: fill color (if specified)
        - group: grouping variable (if group_var is True)

    Examples
    --------
    ```python

    ```
    """

    ###############################################################################
    # Input Checks
    ###############################################################################

    ###############################################################################
    # Data Generation
    ###############################################################################
