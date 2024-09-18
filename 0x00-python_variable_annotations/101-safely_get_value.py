#!/usr/bin/env python3
"""more annotations"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary-like object.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key
        if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
