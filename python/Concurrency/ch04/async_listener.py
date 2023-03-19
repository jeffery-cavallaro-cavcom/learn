"""
Defines an asynchronous context for a listening socket.
"""

import asyncio
import socket

from utils.listener import listener

class AsyncListener(socket.socket):
    """ Listening Socket Context """
    address : tuple[str, int]

    def __init__(self, address : tuple[str, int]):
        """ Create a listening socket """
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address

    async def __aenter__(self) -> 'AsyncListener':
        """ Start listening """
        listener(self, self.address)
        print(f"Listen: {self.address}")
        return self

    async def __aexit__(self, *args, **kwargs) -> None:
        """ Stop listening """
        self.close()
        print(f"\nClosed: {self.address}")

async def main(address : tuple[str, int]) -> None:
    """ Run the listener """
    async with AsyncListener(address) as server:
        loop = asyncio.get_event_loop()
        while True:
            client, peer = await loop.sock_accept(server)
            print(f"Connected: {peer}")
            await loop.sock_sendall(client, b'Hello, World !!!\r\n')
            client.close()
            print(f"Closed: {peer}")

if __name__ == '__main__':
    try:
        asyncio.run(main(('', 8000)))
    except KeyboardInterrupt:
        pass
