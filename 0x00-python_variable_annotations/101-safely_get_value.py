#!/usr/bin/env python3
"""safe_get_value"""
from typing import Mapping, TypeVar, Any, Union, Sequence


T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """safe_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default