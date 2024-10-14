#!/usr/bin/env python3
'''async function to run another aysyn function'''
import asyncio
import random
from 0-basic_async_syntax import wait_random


async def wait_n(n, max_delay):
    '''
    async function to call wait_random a couple of times
    and record its retun values
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return new_list
