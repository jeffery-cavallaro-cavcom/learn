"""
Demonstrates the use of asyncio sleep in a hello world program.
"""

import asyncio

class Hello:
    """ Delayed Hello """
    @staticmethod
    async def say_hello() -> str:
        """ Delayed hello """
        await asyncio.sleep(5)
        return 'Hello, World !!!'

    @classmethod
    async def main(cls) -> None:
        """ Run the coroutine """
        message = await cls.say_hello()
        print(message)

if __name__ == '__main__':
    asyncio.run(Hello.main())
