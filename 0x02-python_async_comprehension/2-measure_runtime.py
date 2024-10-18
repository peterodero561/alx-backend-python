#!/usr/bin/env python3
'''a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''execute async_comprehension four times in parallel using asyncio.gather
    and should measure the total runtime and return it.'''
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = time.perf_counter()
    total = end - start
    return total
