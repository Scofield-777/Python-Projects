#!/usr/bin/env python
import scapy.all as scapy
import argparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        clients_dictionary = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dictionary)
    return clients_list
def print_results(results_list):
    # extract results in better format eg(tabular format)
    print("_______________________________________________________________________")
    print("IP\t\t\tMAC Address")
    print("_______________________________________________________________________")
    for client in results_list:
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
        print(client["ip"] + "\t\t" + client["mac"])
        print("-----------------------------------------------------------------------")
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options = parser.parse_args()
    return options
scan_result = scan("192.168.43.1/24")
print_results(scan_result)
