"""
Demonstrates the use of an asyncio task.
"""

import asyncio
from utils.delay import delay

async def main() -> None:
    """ Run the task """
    task = asyncio.create_task(delay(3))
    print(task)
    result = await task
    print(f"result={result}")

if __name__ == '__main__':
    asyncio.run(main())
