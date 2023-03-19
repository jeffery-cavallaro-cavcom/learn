"""
Demonstrates the asyncio gather method.
"""

import asyncio
import sys

from aiohttp import ClientSession, ClientTimeout

from utils.timed import timed
from utils.webquery import webquery

@timed()
async def main(url : str, count : int) -> None:
    """ Do simultaneous web queries """
    timeout = ClientTimeout(total=5)
    async with ClientSession(timeout=timeout) as session:
        urls = ['http://www.notastie.com']
        urls += [url] * count
        urls.append('xxx://www.example.com')
        status_codes = await asyncio.gather(
            *[webquery(session, url) for url in urls],
            return_exceptions=True
        )
    print(status_codes)

if __name__ == '__main__':
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) >= 2 else 'http://www.example.com',
            10
        )
    )
