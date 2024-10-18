#!/usr/bin/env python3
'''async function to run another aysyn function'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    async function to call wait_random a couple of times
    and record its retun values
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
