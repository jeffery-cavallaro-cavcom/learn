"""
Demonstrates running a normal function versus a coroutine.
"""

import asyncio

class Incrementer:
    """ Increment Methods """
    @staticmethod
    def normal_add_one(number : int) -> int:
        """ Add one (no coroutine) """
        return number + 1

    @staticmethod
    async def coroutine_add_one(number : int) -> int:
        """ Add one (coroutine) """
        return number + 1

    @classmethod
    async def main(cls) -> None:
        """ Run two coroutines """
        result1 = await cls.coroutine_add_one(1)
        result2 = await cls.coroutine_add_one(2)
        print(f"result1={result1}, result2={result2}")

def run() -> None:
    """ Run the coroutines """
    normal_result = Incrementer.normal_add_one(1)
    coroutine_result = Incrementer.coroutine_add_one(1)

    print(f"NORMAL: {normal_result}")
    print(f"COROUTINE: {coroutine_result}")

    run_result = asyncio.run(coroutine_result)
    print(f"RUN: {run_result}")

    asyncio.run(Incrementer.main())

if __name__ == '__main__':
    run()
