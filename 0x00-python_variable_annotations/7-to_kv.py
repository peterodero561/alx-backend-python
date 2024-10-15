#!/usr/bin/env python3
'''Function to return a tuple'''
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple of the given parameters'''
    return (k, v)
