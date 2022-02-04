import json
import socket
import threading

from block import Block


class Server:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._socket = None
        self._thread = None

        self._connections = [{
            "host": host,
            "port": port
        }]

        self._blockchain = [
            Block(0, None)
        ]

        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._socket.bind((host, port))

            self._thread = threading.Thread(target=self._listen)
            self._thread.start()
        except:
            print("Error: Couldn't start the server at %s::%s" % (host, port))

    def _send_connections(self):
        for destination in self._connections:
            for connection in self._connections:
                request = {
                    "type": "connection",
                    "host": connection["host"],
                    "port": connection["port"]
                }

                request = json.dumps(request)
                request = request.encode(encoding="utf8")

                self._socket.sendto(request, (destination["host"], destination["port"]))

    def _sync_connection(self, request: json):
        connection = {
            "host": request["host"],
            "port": request["port"]
        }

        if connection not in self._connections:
            self._connections.append(connection)

    def _send_blocks(self):
        for destination in self._connections:
            for block in self._blockchain:
                if block != None:
                    request = {
                        "type": "block",
                        "index": block.get_json()["index"],
                        "data": block.get_json()["data"]
                    }

                    request = json.dumps(request)
                    request = request.encode(encoding="utf8")

                    self._socket.sendto(request, (destination["host"], destination["port"]))

    def _sync_block(self, request: json):
        if request["index"] == len(self._blockchain):
            block = Block(request["index"], request["data"])
            self._blockchain.append(block)
        elif request["index"] < len(self._blockchain):
            if self._blockchain[request["index"]] == None:
                block = Block(request["index"], request["data"])
                self._blockchain[request["index"]] = block
            else:
                if self._blockchain[request["index"]].data == request["data"]:
                    self._blockchain[request["index"]].vote(True)
                else:
                    self._blockchain[request["index"]].vote(False)

                if self._blockchain[request["index"]].request_counter == 100:
                    if self._blockchain[request["index"]].agrees < self._blockchain[request["index"]].disagrees:
                        self._blockchain[request["index"]] = None
                    else:
                        self._blockchain[request["index"]].request_counter = 0
                        self._blockchain[request["index"]].agrees = 0
                        self._blockchain[request["index"]].disagrees = 0

    def _listen(self):
        while True:
            self._send_connections()
            self._send_blocks()

            request = self._socket.recv(1024)
            request = request.decode(encoding="utf8")
            request = json.loads(request)

            if request["type"] == "connection":
                self._sync_connection(request)
            elif request["type"] == "block":
                self._sync_block(request)

    def add_connection(self, host: str, port: int):
        connection = {
            "host": host,
            "port": port
        }

        self._connections.append(connection)

    def add_block(self, data: str):
        block = Block(len(self._blockchain), data)
        self._blockchain.append(block)

    def print_server_data(self):
        index = 0

        print("%s::%s {" % (self._host, self._port))
        print(" \"connections\":\"%s\"" % self._connections)
        print(" \"blockchain\": [")

        for block in self._blockchain:
            print("  %s {" % index)

            if block == None:
                print("   None")
            else:
                print("   \"data\":\"%s\"" % block.data)
                print("   \"request_counter\":\"%s\"" % block.request_counter)
                print("   \"agrees\":\"%s\"" % block.agrees)
                print("   \"disagrees\":\"%s\"" % block.disagrees)

            index += 1
            print("  }")

        print(" ]")
        print("}")
