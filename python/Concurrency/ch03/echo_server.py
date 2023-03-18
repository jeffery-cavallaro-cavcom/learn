"""
A TCP server that accepts client connections and echos all received data
back to the client.
"""

from dataclasses import dataclass
import socket
import selectors
from typing import ClassVar

from utils.listener import listener

@dataclass
class ClientConnection:
    """ A single client connection """
    address : tuple[str, int]
    buffer : bytes

class EchoServer(socket.socket):
    """ Echo Server """
    ADDR : ClassVar[str] = ('', 8000)

    connections : dict[socket.socket, ClientConnection]
    selector : selectors.DefaultSelector

    def __init__(self):
        """ Create a listening socket """
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        listener(self, self.ADDR)

        self.connections = {}
        self.selector = selectors.DefaultSelector()

    def run(self) -> None:
        """ Run the server """
        self.selector.register(self, selectors.EVENT_READ)

        try:
            while True:
                events = self.selector.select(timeout=10)
                if len(events) <= 0:
                    print('No events, waiting')
                    continue

                for event, _ in events:
                    active = event.fileobj
                    if active == self:
                        try:
                            client, address = self.accept()
                        except BlockingIOError:
                            continue

                        self.add_client(client, address)
                    else:
                        self.service_client(active)
        except KeyboardInterrupt:  # pylint: disable=broad-except
            print('\nExiting')

        self.cleanup()

    def add_client(self, client : socket.socket, address : tuple[str, int]):
        """ Add a new client """
        client.setblocking(False)
        self.selector.register(client, selectors.EVENT_READ)
        self.connections[client] = ClientConnection(address, b'')

        print(f"Connect: {address}")

    def service_client(self, client : socket.socket) -> None:
        """ Get and echo client bytes """
        connection = self.connections.get(client, None)
        if not connection:
            return

        try:
            data = client.recv(16)
        except BlockingIOError:
            return

        nbytes = len(data)
        print(f"Received: {connection.address}: {nbytes} bytes")

        if nbytes <= 0:
            print(f"Disconnect: {connection.address}")
            self.remove_client(client)

        connection.buffer += data
        if len(connection.buffer) >= 2 and connection.buffer[-2:] == b'\r\n':
            client.sendall(connection.buffer)
            print(f"Send: {connection.address}: {connection.buffer}")
            connection.buffer = b''

    def remove_client(self, client : socket.socket) -> None:
        """ Close and remove a client """
        self.selector.unregister(client)

        connection = self.connections.pop(client, None)
        if not connection:
            return

        print(f"Close: {connection.address}")
        try:
            client.close()
        except Exception as error:  # pylint: disable=broad-except
            print(f"Error closing {connection.address}: {str(error)}")

    def cleanup(self) -> None:
        """ Close existing connections """
        for client in list(self.connections.keys()):
            self.remove_client(client)

if __name__ == '__main__':
    with EchoServer() as server:
        server.run()
