#!/usr/bin/env python3
'''function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier.'''


def make_multiplier(multiplier: float):
    '''returns a function that multiplies a float by multiplier.'''
    def mult_multiplier(mult: float) -> float:
        '''retuns multiplier muiltiplied by a float'''
        return mult * multiplier
    return mult_multiplier
