"""
A reimplementation of the echo server using asynio.
"""

import asyncio
import signal
import socket
from typing import ClassVar

from utils.listener import listener

class AsyncEchoServer(socket.socket):
    """ Asyncio-implemented Echo Server """
    ADDR : ClassVar[str] = ('', 8000)

    loop : asyncio.AbstractEventLoop
    accepter : asyncio.Task
    connections : dict[socket.socket, asyncio.Task]
    done : bool

    def __init__(self):
        """ Create a listening socket """
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        listener(self, self.ADDR)

        self.loop = None
        self.accepter = None
        self.connections = {}
        self.done = True

    def shutdown(self) -> None:
        """ Initiate shutdown """
        if self.accepter:
            self.accepter.cancel()
        self.done = True

    async def main(self) -> None:
        """ Run the main task """
        self.done = False

        self.loop = asyncio.get_event_loop()

        for signo in [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]:
            self.loop.add_signal_handler(signo, self.shutdown)

        self.accepter = self.loop.create_task(self.accept_connections())
        await self.accepter

        print('\nExiting...')

    async def accept_connections(self) -> None:
        """ Accept client connections """

        try:
            while not self.done:
                client, address = await self.loop.sock_accept(self)
                print(f"Connected: {address}")

                client.setblocking(False)
                client_task = self.loop.create_task(self.echoer(client, address))
                self.connections[client] = client_task

                print(f"Connections: {len(self.connections)}")
        except asyncio.CancelledError:
            pass
        except Exception as error:  # pylint: disable=broad-except
            print(f"Accept: {str(error)}")

    async def echoer(self, client : socket.socket,
                     address : tuple[str, int]) -> None:
        """ Echo client data """
        buffer = b''

        try:
            while True:
                data = await self.loop.sock_recv(client, 16)
                print(f"Received: {address}: size={len(data)}")
                if len(data) <= 0:
                    print(f"Disconnected: {address}")
                    break
                buffer += data
                if len(buffer) >= 2 and buffer[-2:] == b'\r\n':
                    await self.loop.sock_sendall(client, buffer)
                    print(f"Sent: {address}: data={buffer}")
                    buffer = b''
        except asyncio.CancelledError:
            pass
        except Exception as error:  # pylint: disable=broad-except
            print(f"Error: {address}: {str(error)}")
        finally:
            self.connections.pop(client)
            client.close()
            print(f"Closed: {address}")
            print(f"Remaining: {len(self.connections)}")

if __name__ == '__main__':
    asyncio.run(AsyncEchoServer().main())
