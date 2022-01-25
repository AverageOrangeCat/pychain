import socket
import threading
import sys
import json

class Pychain:
    def __init__(self, host: str, port: int):
        self._sock = None
        self._thread = threading.Thread(target=self._listen, args=(0,))
        self._connections = [[host, port]]

        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._sock.bind((host, port))
        except socket.error:
            print("Error: Could not setup socket.")
            sys.exit(1)

        self._thread.start()

    def _send(self, host: str, port: int):
        req = {
            "connections": self._connections,
        }

        req = json.dumps(req)
        req = req.encode(encoding="utf-8")
        self._sock.sendto(req, (host, port))

    def _broadcast(self):
        for connection in self._connections:
            self._send(connection[0], connection[1])

    def _sync(self, req: json):
        for connection in req["connections"]:
            if connection not in self._connections:
                self._connections.append(connection)

    def _listen(self, kwargs):
        while True:
            self._broadcast()

            req = self._sock.recv(1024)
            req = req.decode(encoding="utf-8")
            req = json.loads(req)

            self._sync(req)

    def add_connection(self, host: str, port: int):
        if [host, port] not in self._connections:
            self._connections.append([host, port])

    def get_connections(self, id: str):
        print("%s::%s" % (id, self._connections))