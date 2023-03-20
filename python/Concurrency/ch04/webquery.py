"""
Demonstrates how to do asynchronous web queries with aiohttp and the various
ways to wait for the results.
"""

import argparse
import asyncio
import random
from typing import ClassVar, Optional

from aiohttp import ClientSession, ClientTimeout

from utils.timed import timed

class WebQuery:
    """ Do Web Queries and Check Results """
    GOOD : ClassVar[str] = 'http://www.example.com'
    BAD : ClassVar[str] = 'http://www.notasite.com'
    UGLY : ClassVar[str] = 'httpx://www.example.com'

    arguments : argparse.Namespace

    def __init__(self):
        """ Initialize a new query context """
        self.arguments = self.get_arguments()

    @classmethod
    def get_arguments(cls) -> argparse.Namespace:
        """ Parse command line arguments """
        parser = argparse.ArgumentParser(description='Asynchronous web queries')
        mutex = parser.add_mutually_exclusive_group()

        mutex.add_argument(
            '-a', '--as_completed', action='store_true', help='use as_completed'
        )
        parser.add_argument(
            '-b', '--bad', action='store_true', help='include bad queries'
        )
        parser.add_argument(
            '-c', '--count', type=int, default=1, help='number of queries'
        )
        parser.add_argument(
            '-d', '--delay', type=int, help='delay before each query'
        )
        mutex.add_argument(
            '-g', '--gather', action='store_true', help='use gather'
        )
        parser.add_argument(
            '-s', '--stopwatch', action='store_true', help='time each query'
        )
        parser.add_argument(
            '-t', '--timeout', type=int, default=5, help='session timeout (s)'
        )
        mutex.add_argument(
            '-w', '--wait', type=int, help="use wait: AC(1), FE(2), FC(3)"
        )
        parser.add_argument(
            'url', nargs='?', default=cls.GOOD, help='URL to query'
        )

        return parser.parse_args()

    @timed()
    async def main(self) -> None:
        """ Query a URL """
        timeout = ClientTimeout(total=self.arguments.timeout)
        method = (
            self.timed_webquery if self.arguments.stopwatch else self.webquery
        )
        delay = self.arguments.delay
        loop = asyncio.get_event_loop()

        async with ClientSession(timeout=timeout) as session:
            tasks = [
                loop.create_task(
                    method(
                        session,
                        self.arguments.url,
                        delay=(
                            delay if delay
                            else (
                                random.randint(0, 10)
                                if (
                                    self.arguments.as_completed or
                                    self.arguments.wait
                                )
                                else 0
                            )
                        )
                    )
                )
                for _ in range(self.arguments.count)
            ]
            if self.arguments.bad:
                tasks = [
                    loop.create_task(method(session, self.BAD, delay=delay)),
                    *tasks,
                    loop.create_task(method(session, self.UGLY, delay=delay)),
                ]

            if self.arguments.gather:
                await self.gather_results(tasks)
            elif self.arguments.as_completed:
                await self.as_completed_results(tasks)
            elif self.arguments.wait is not None:
                await self.wait_results(tasks, self.arguments.wait)
            else:
                await self.get_results(tasks)

    @staticmethod
    async def gather_results(tasks : list[asyncio.Task]) -> None:
        """ Get task results via gather """
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for iresult, result in enumerate(results):
            print(f"[{iresult}] = {repr(result)}")

    @staticmethod
    async def as_completed_results(tasks : list[asyncio.Task]) -> None:
        """ Get task results via as completed """
        for itask, task in enumerate(asyncio.as_completed(tasks)):
            print(f"[{itask}] = {repr(await task)}")

    @staticmethod
    async def wait_results(tasks : list[asyncio.Task], code : int):
        """ Wait for results """
        if code == 2:
            wait_type = asyncio.FIRST_EXCEPTION
        elif code == 3:
            wait_type = asyncio.FIRST_COMPLETED
        else:
            wait_type = asyncio.ALL_COMPLETED

        running = tasks
        itask = 0

        while running:
            done, running = await asyncio.wait(running, return_when=wait_type)
            print(f"DONE: {len(done)}; RUNNING={len(running)}")

            for task in done:
                if task.exception():
                    print(f"[{itask}] = {repr(task.exception())}")
                else:
                    print(f"[{itask}] = {repr(task.result())}")
                itask += 1

    @staticmethod
    async def get_results(tasks : list[asyncio.Task]) -> None:
        """ Get task results """
        results = [await task for task in tasks]
        for iresult, result in enumerate(results):
            print(f"[{iresult}] = {repr(result)}")

    @timed()
    async def timed_webquery(
        self, session : ClientSession, url : str, delay : Optional[int] = None
    ) -> int:
        """ Perform a timed web query """
        return await self.webquery(session, url, delay)

    @staticmethod
    async def webquery(
        session : ClientSession, url : str, delay : Optional[int] = None
    ) -> int:
        """ Perform a web query """
        try:
            if delay:
                await asyncio.sleep(delay)
            async with session.get(url) as response:
                status = response.status
        except asyncio.TimeoutError:
            status = 'Timeout!'
        except asyncio.CancelledError:
            status = 'Cancelled!'

        return status

if __name__ == '__main__':
    asyncio.run(WebQuery().main())
