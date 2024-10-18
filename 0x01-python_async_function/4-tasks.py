#!/usr/bin/env python3
'''async function to run another aysyn function'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''async function to call wait_random a couple of times and
    record its retun values'''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
