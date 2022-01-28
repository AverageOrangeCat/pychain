import socket
import threading
import sys
import json

class Pychain:
    def __init__(self, host: str, port: int):
        self._sock = None
        self._thread = threading.Thread(target=self._listen, args=(0,))
        self._connections = [[host, port]]
        self._chunks = []

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
            "chunks": self._chunks,
        }

        req = json.dumps(req)
        req = req.encode(encoding="utf-8")
        self._sock.sendto(req, (host, port))

    def _broadcast(self):
        for connection in self._connections:
            self._send(connection[0], connection[1])

    def _sync_connections(self, req: json):
        for connection in req["connections"]:
            if connection not in self._connections:
                self._connections.append(connection)

        self._connections.sort()

    def _sync_chunks(self, req: json):
        for chunk in req["chunks"]:
            if chunk not in self._chunks:
                self._chunks.append(chunk)

        self._chunks.sort()

    def _listen(self, kwargs):
        while True:
            self._broadcast()

            req = self._sock.recv(1024)
            req = req.decode(encoding="utf-8")
            req = json.loads(req)

            self._sync_connections(req)
            self._sync_chunks(req)

    def print_data(self, id: str):
        print("%s {" % id)
        print(" connections: %s" % self._connections)
        print(" chunks: %s" % self._chunks)
        print("}")

    def add_connection(self, host: str, port: int):
        if [host, port] not in self._connections:
            self._connections.append([host, port])

    def add_chunk(self, chunk: str):
        if chunk not in self._chunks:
            self._chunks.append(chunk)
