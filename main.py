import time

from server import Server

server_00 = Server("127.0.0.1", 8880)
server_01 = Server("127.0.0.1", 8881)
server_02 = Server("127.0.0.1", 8882)
server_03 = Server("127.0.0.1", 8883)
server_04 = Server("127.0.0.1", 8884)

server_00.print_server_data()
server_01.print_server_data()
server_02.print_server_data()
server_03.print_server_data()
server_04.print_server_data()
print("============================================================================")

server_00.add_connection("127.0.0.1", 8881)
server_00.add_connection("127.0.0.1", 8882)
server_02.add_connection("127.0.0.1", 8883)
server_02.add_connection("127.0.0.1", 8884)

server_00.print_server_data()
server_01.print_server_data()
server_02.print_server_data()
server_03.print_server_data()
server_04.print_server_data()
print("============================================================================")

time.sleep(3)

server_00.print_server_data()
server_01.print_server_data()
server_02.print_server_data()
server_03.print_server_data()
server_04.print_server_data()
print("============================================================================")

server_00.add_block("Hello World!")
server_01.add_block("Go!")

server_00.print_server_data()
server_01.print_server_data()
server_02.print_server_data()
server_03.print_server_data()
server_04.print_server_data()
print("============================================================================")

time.sleep(30)

server_00.print_server_data()
server_01.print_server_data()
server_02.print_server_data()
server_03.print_server_data()
server_04.print_server_data()
print("============================================================================")

print("END!")
