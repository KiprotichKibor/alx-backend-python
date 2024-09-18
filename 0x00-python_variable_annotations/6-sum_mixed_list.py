#!/usr/bin/env python3
""" multiple types annotation """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function to calculate sum of a mixed list
    """
    return float(sum(mxd_lst))
