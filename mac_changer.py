#!/usr/bin/env python

import subprocess
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def change_mac_address(interface, new_mac):

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changing Mac-Address for " + interface + " to " + new_mac + "\n")
    # subprocess.call(["ifconfig", interface])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_Search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_Search_result:
        return mac_address_Search_result.group(0)
    else:
        print("Not a valid mac address or interface")

# Will get the arguments that the user has entered...
options = get_args()

# Will return the current mac address
current_mac = get_current_mac(options.interface)
print("Current Mac: " + str(current_mac))

change_mac_address(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] MAC Address did not get changed")





# interface_type = input("Enter Type of Interface: ")
# new_mac_address = input("Enter New Mac(eg: 00:11:22:33:44:55): ")

# --------------------------using string structure-------------------------
# subprocess.call("ifconfig " + interface_type + " down", shell=True)
# subprocess.call("ifconfig " + interface_type + " hw ether " + new_mac_address, shell=True)
# subprocess.call("ifconfig " + interface_type + " up", shell=True)



