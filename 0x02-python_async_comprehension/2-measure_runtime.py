#!/usr/bin/env python3
"""Module that measures the runtime of parallel async comprehensions."""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.

    This coroutine uses asyncio.gather to run async_comprehension four times
    concurrently. It measures the total time taken for all four executions
    to complete.

    Returns:
        float: The total runtime in seconds.

    Example:
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime} seconds")
    """
    start_time = time.perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
