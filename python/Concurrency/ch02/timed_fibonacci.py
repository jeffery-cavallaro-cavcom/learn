"""
Calculates Fibonacci numbers in a brute force, inefficient manner with yields
every 10 levels for an in-progress report.
"""

import asyncio
import time

class TimedFibonacci:
    """ Timed Fibonacci Calculator """
    done : bool

    def __init__(self):
        """ Reset done flag """
        self.done = False

    async def calculate(self, number: int) -> int:
        """ Calculate a Fibonacci number """
        self.done = False

        fib1 = 0
        fib2 = 1

        if number <= 1:
            answer = fib1
        elif number == 2:
            answer = fib2
        else:
            for trial in range(number - 2):
                if (trial % 10) == 0:
                    print(f"level={trial}")
                    await asyncio.sleep(1)
                answer = fib1 + fib2
                fib1 = fib2
                fib2 = answer

        self.done = True

        return answer

    async def status(self) -> None:
        """ Report status until done """
        while not self.done:
            print('Calculating ...')
            await asyncio.sleep(5)

    async def main(self, number : int) -> int:
        """ Run Fibonacci calculation """
        start = time.time()
        fib_task = asyncio.create_task(self.calculate(number))
        timer_task = asyncio.create_task(self.status())
        result = await fib_task
        end = time.time()
        await timer_task
        print(f"time={end - start:.4f}")
        return result

if __name__ == '__main__':
    print(f"result={asyncio.run(TimedFibonacci().main(100))}")
