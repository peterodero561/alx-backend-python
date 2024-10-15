#!/usr/bin/env python3
'''Returns the first element of the list if it exists,
otherwise returns None.'''
from typing import Any, Optional, Iterable


def safe_first_element(lst: Iterable[Any]) -> Optional[Any]:
    '''Returns the first element of the list if it exists,
    otherwise returns None.'''
    if lst:
        return lst[0]
    else:
        return None
