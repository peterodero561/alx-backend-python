#!/usr/bin/env python3
'''Annotate to and return values with the appropriate types'''
from typing import Union, List, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    '''returns the elements of a list with appropiate values'''
    return [(i, len(i)) for i in lst]
