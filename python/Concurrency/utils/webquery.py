"""
Performs an asynchronous web query.
"""

import asyncio
from aiohttp import ClientSession

from utils.timed import timed

@timed()
async def timed_webquery(session : ClientSession, url : str) -> int:
    """ Perform a timed web query """
    return await webquery(session, url)

async def webquery(session : ClientSession, url : str) -> int:
    """ Perform a web query """
    try:
        async with session.get(url) as response:
            status = response.status
    except asyncio.TimeoutError:
        status = 'Timeout!'

    return status
