"""
Creates a listening socket.
"""

import socket

def listener(
        server : socket.socket,
        address : tuple[str, int],
        blocking : bool = False
        ) -> None:
    """ Create a listening socket """
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.setblocking(bool(blocking))
    server.bind(address)
    server.listen()
