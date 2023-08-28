#!/usr/bin/env python
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting to the destination and we have used two brackets as it accepts values in the form of tuples
connection.connect(("192.168.43.198", 4444))

# send data
message = "[+]Connection Established.\n"

# Encode String
byte = message.encode()
connection.send(byte)

# Receive Data
receive_data = connection.recv(1024)
# 1024 bytes of buffer size

# Decode String
e_data = receive_data.decode()
print(e_data)

# Close Connection
connection.close()
