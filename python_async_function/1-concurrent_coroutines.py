#!/usr/bin/env python3
"""
 function that returns the list of all the task
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the task
    """
    delay_list = []
    for i in range(n):
        delay_list.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delay_list)]
