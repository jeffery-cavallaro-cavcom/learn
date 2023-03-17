"""
Demonstrates the timed decorator.
"""

import asyncio
from utils.timed import timed

@timed()
async def delay(duration : int) -> int:
    """ Wait for a while """
    print(f"Sleeping for {duration} second(s)")
    await asyncio.sleep(duration)
    print(f"Awake after {duration} seconds")
    return duration

@timed()
async def main() -> None:
    """ Run delay tasks """
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

asyncio.run(main())
