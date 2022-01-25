import shlex

command = []

print("---{ PYCHAIN V.1.0.0 }---")

while True:
    command = shlex.split(input(">> "))

    if len(command) == 1 and command[0] == "help":
        print("---{ HELP }---")
        print("- exit")
        print("- connect <HOST> <PORT>")
    elif len(command) == 1 and command[0] == "exit":
        break
    elif len(command) == 3 and command[0] == "connect":
        continue
    else:
        print("Error: Invalid command '%s'" % shlex.join(command))
