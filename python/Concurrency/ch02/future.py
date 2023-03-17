"""
Demonstrates the use of a future.
"""

import asyncio

class FutureSetter:
    """ Manage a Future """
    future : asyncio.Future

    def __init__(self):
        """ Initialize a future """
        self.future = None

    async def set_future(self) -> None:
        """ Set the future value after a delay """
        await asyncio.sleep(5)
        self.future.set_result(42)

    def make_task(self) -> None:
        """ Run the set value task """
        self.future = asyncio.Future()
        asyncio.create_task(self.set_future())

    async def main(self):
        """ Set and check future value """
        self.make_task()
        print(f"done={self.future.done()}")
        value = await self.future
        print(f"done={self.future.done()}")
        print(f"value={value}")

if __name__ == '__main__':
    asyncio.run(FutureSetter().main())
