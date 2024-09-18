#!/usr/bin/env python3
""" function annotation """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float
        and returns a float.
    """
    def multiplier_function(n: float) -> float:
        return multiplier * n

    return multiplier_function
