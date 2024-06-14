#!/usr/bin/env python3
"""
Module that defines a function called measure_runtime
"""

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """function called measure_runtime"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    return time.time() - start
