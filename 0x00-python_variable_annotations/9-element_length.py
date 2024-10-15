#!/usr/bin/env python3
'''Annotate to and return values with the appropriate types'''
from typing import Tuple, Iterable, Sequence, List


def element_length(lst: Iterable[Sequence])-> List[Tuple[Sequence, int]]:
    '''returns the elements of a list with appropiate values'''
    return [(i, len(i)) for i in lst]
