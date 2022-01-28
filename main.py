from pychain import Pychain
import shlex
import sys

print("---{ PYCHAIN V.1.0.0 }---")
host = input("Host: ")
port = input("Port: ")

server = Pychain(host, int(port))
command = []

while True:
    command = shlex.split(input(">> "))

    if len(command) == 1 and command[0] == "help":
        print("---{ HELP }---")
        print("- connect <HOST> <PORT>")
        print("- chunk <MESSAGE>")
        print("- info")
    if len(command) == 3 and command[0] == "connect":
        server.add_connection(command[1], int(command[2]))
    elif len(command) == 2 and command[0] == "chunk":
        server.add_chunk(command[1])
    elif len(command) == 1 and command[0] == "info":
        server.print_data("%s::%s" % (host, port))
    else:
        print("Error: Invalid command '%s'" % shlex.join(command))
