#!/usr/bin/env python3
'''a coroutine called async_generator that takes no arguments.'''
import asyncio
import random


async def async_generator():
    '''Coroutine that yields a random number between 0 and 10, 10 times,
    with a 1-second delay between each.'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
