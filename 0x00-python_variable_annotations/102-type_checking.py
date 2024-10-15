#!/usr/bin/env python3
'''Returns a zoomed-in version of the input list or tuple.'''
from typing import List, Tuple, Union


def zoom_array(lst: Union[List[int], Tuple[int, ...]], factor: int = 2) -> List[int]:
    '''Returns a zoomed-in version of the input list or tuple.'''
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)  # Using `_` for an unused variable
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

# Call with an integer factor
zoom_3x = zoom_array(array, 3)  # Changed 3.0 to 3 (integer)
