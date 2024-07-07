#!/usr/bin/env python3
"""
Given the parameters and return values, add type annotations to the function
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with key in dct if it exists, otherwise
    returns default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
