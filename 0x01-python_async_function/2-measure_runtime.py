#!/usr/bin/env python3
"""Module for measuring the runtime of wait_n."""

import time
import asyncio
from typing import Union


wait_n = __import__(1-concurrent_coroutines).wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: Average time per call (total_time / n).
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
