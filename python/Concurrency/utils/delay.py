"""
Prints messages with a delay in between messages.
"""

import asyncio
async def delay(delay_seconds : int) -> int:
    """ Print, sleep, print """
    print(f"Sleeping for {delay_seconds} second(s)")
    await asyncio.sleep(delay_seconds)
    print(f"Finished sleeping for {delay_seconds} seconds(s)")
    return delay_seconds

if __name__ == '__main__':
    asyncio.run(delay(5))
