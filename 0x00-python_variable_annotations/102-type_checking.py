#!/usr/bin/env python3
"""
Mypy
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Creates a zoomed-in version of a tuple by repeating each element.

    Args:
        lst (Tuple): The input tuple to be zoomed.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        List: A new list where each element from the input tuple is repeated
              'factor' number of times.

    Example:
        >>> zoom_array((1, 2, 3), 2)
        [1, 1, 2, 2, 3, 3]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
