#!/usr/bin/emv python3
"""
Annotate the below function’s parameters and return values with the
appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
