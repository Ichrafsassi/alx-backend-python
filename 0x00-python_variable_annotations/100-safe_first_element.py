#!/usr/bin/env python3
"""Safe_first_element"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe_first_element: takes a list and returns its first element"""
    if lst:
        return lst[0]
    else:
        return None
