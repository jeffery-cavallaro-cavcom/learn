"""
Demonstrates the use of asyncio tasks.
"""

import asyncio
from utils.delay import delay

class Adder:
    """ Add methods """
    @staticmethod
    async def add_one(number : int) -> int:
        """ Increment """
        return number + 1

    @staticmethod
    async def hello(seconds : int) -> str:
        """ Delayed hello """
        await delay(seconds)
        return 'Hello, World !!!'

    @classmethod
    async def main(cls) -> None:
        """ Run the tasks """
        hello_task = asyncio.create_task(cls.hello(3))
        add_task = asyncio.create_task(cls.add_one(1))
        result = await add_task
        print(f"result={result}")
        message = await hello_task
        print(f"message={message}")

if __name__ == '__main__':
    asyncio.run(Adder.main())
