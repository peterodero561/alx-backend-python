#!/usr/bin/env python3
'''Function to sum up a list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union(int, float])) -> float:
    '''returs sum of the elements of a list'''
    return sum(mxd_lst)
