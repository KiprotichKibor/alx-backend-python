#!/usr/bin/env python3
"""Module that defines an asynchronous generator function."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields random numbers.

    This coroutine loops 10 times. In each iteration, it waits asynchronously
    for 1 second and then yields a random float between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
