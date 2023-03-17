"""
Demostrates task timeout.
"""

import asyncio
from utils.delay import delay

async def main() -> None:
    """ Time out a task """
    delay_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(delay_task, timeout=5)
        print(f"result={result}")
    except asyncio.exceptions.TimeoutError:
        print('Timeout!')
        print(f"canceled={delay_task.cancelled()}")

asyncio.run(main())
