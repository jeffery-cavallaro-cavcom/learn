"""
Demostrates task timeout with a shield to prevent cancellation.
"""

import asyncio
from utils.delay import delay

async def main() -> None:
    """ Time out a task """
    shield_task = asyncio.create_task(delay(10))

    try:
        result = await asyncio.wait_for(asyncio.shield(shield_task), timeout=5)
        print(f"result={result}")
    except asyncio.exceptions.TimeoutError:
        print('Timeout!')
        print(f"canceled={shield_task.cancelled()}")
        result = await shield_task
        print(f"result={result}")

asyncio.run(main())
