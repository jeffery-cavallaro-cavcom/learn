"""
Demonstrates canceling a task.
"""

import asyncio
from utils.delay import delay

async def main() -> None:
    """ Cancel a task """
    long_task = asyncio.create_task(delay(10))

    elapsed = 0

    while not long_task.done():
        print('Task not done')
        await asyncio.sleep(1)
        elapsed += 1
        if elapsed >= 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print('Task canceled')

asyncio.run(main())
