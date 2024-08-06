#!/usr/bin/env python3
"""Module for wait_random coroutine."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay waited.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
