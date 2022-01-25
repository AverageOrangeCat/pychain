from pychain import Pychain
import time

server_00 = Pychain("127.0.0.1", 8880)
server_01 = Pychain("127.0.0.1", 8881)
server_02 = Pychain("127.0.0.1", 8882)
server_03 = Pychain("127.0.0.1", 8883)
server_04 = Pychain("127.0.0.1", 8884)

server_00.add_connection("127.0.0.1", 8880)
server_00.add_connection("127.0.0.1", 8881)
server_00.add_connection("127.0.0.1", 8882)
server_01.add_connection("127.0.0.1", 8883)
server_01.add_connection("127.0.0.1", 8884)

while True:
    server_00.get_connections("server_00")
    server_01.get_connections("server_01")
    server_02.get_connections("server_02")
    server_03.get_connections("server_04")
    server_04.get_connections("server_05")
    print("")
    time.sleep(3)
