"""
Demonstrates multiple, concurrent tasks.
"""

import asyncio
from utils.delay import delay

async def main() -> None:
    """ Run sleeper tasks """
    task1 = asyncio.create_task(delay(1))
    task2 = asyncio.create_task(delay(2))
    task3 = asyncio.create_task(delay(3))

    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(main())
