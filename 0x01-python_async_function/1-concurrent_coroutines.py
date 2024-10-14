#!/usr/bin/env python3
'''async function to run another aysyn function'''
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    '''
    async function to call wait_random a couple of times
    and record its retun values
    '''
    new_list = []
    for i in range(n):
        delay = await wait_random(max_delay)
        new_list.append(delay)

    return new_list
