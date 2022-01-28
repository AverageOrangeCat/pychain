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

server_00.add_chunk("Hello World!")
server_01.add_chunk("AWSOME!!!")

while True:
    server_00.print_data("server_00")
    server_01.print_data("server_01")
    server_02.print_data("server_02")
    server_03.print_data("server_03")
    server_04.print_data("server_04")
    print("===========================================================================")
    time.sleep(3)
