"""
Demonstrates the event loop's debug mode.
"""

import asyncio
from utils.timed import timed

@timed()
async def cpu_bound_work() -> int:
    """ Delay counter """
    counter = 0
    for _ in range(1000000000):
        counter += 1
    return counter

async def main() -> None:
    """ Run CPU-bound work """
    asyncio.get_event_loop().slow_callback_duration = 5.0
    task = asyncio.create_task(cpu_bound_work())
    await task

asyncio.run(main(), debug=True)
