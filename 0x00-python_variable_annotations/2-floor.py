#!/usr/bin/env python3
""" Floor math function """
import math


def floor(n: float) -> int:
    """
    Calculate the floor of a given float number.

    Args:
        n (float): The number to calculate the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
