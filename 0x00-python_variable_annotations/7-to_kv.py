#!/usr/bin/env python3
"""to_kv module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv: takes a string k and an int OR float v as arguments
    Returns:
        Tuple[str, float]: tuple containing k and the square of v
    """
    return (k, float(v**2))
