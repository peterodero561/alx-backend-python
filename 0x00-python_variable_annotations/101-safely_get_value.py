#!/usr/bin/env python3
'''function to return value associated with key'''
from typing import TypeVar, Dict, Optional


K = TypeVar('K')  # Type for keys
V = TypeVar('V')  # Type for values


def safely_get_value(dct: Dict[K, V], key: K, default: Optional[
    V] = None) -> Optional[V]:
    '''Returns the value associated with the key in the
    dictionary if it exists, otherwise returns default.'''
    if key in dct:
        return dct[key]
    else:
        return default
