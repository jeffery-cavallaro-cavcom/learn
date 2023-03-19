"""
Performs an asynchronous web query.
"""

import asyncio
import sys

from aiohttp import ClientSession, ClientTimeout

from utils.webquery import timed_webquery
from utils.timed import timed

@timed()
async def main(url : str) -> None:
    """ Query a URL """
    timeout = ClientTimeout(total=5)
    async with ClientSession(timeout=timeout) as session:
        status = await timed_webquery(session, url)
        print(f"status={status}")

if __name__ == '__main__':
    asyncio.run(
        main(sys.argv[1] if len(sys.argv) >= 2 else 'http://www.example.com')
    )
