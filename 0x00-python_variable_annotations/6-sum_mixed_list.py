#!/usr/bin/env python3
"""sum_mixed_list module file"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats
    Returns their sum as a float
    Args:
        mxd_lst: list of floats+integers
    """
    return sum(mxd_lst)
