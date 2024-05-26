# DNS Spoofing Script

This Python script allows you to perform DNS (Domain Name System) spoofing by modifying DNS responses to redirect traffic to a specified IP address.

## Prerequisites

- Python 3.x
- Required Python packages: `netfilterqueue`, `scapy`

## Usage

1. Make sure you have Python installed on your system.
2. Install the necessary Python packages by running:

   ```bash
   pip install netfilterqueue scapy
3. Enable IP forwarding on your system by running:

  ```bash
  Copy code
  echo 1 > /proc/sys/net/ipv4/ip_forward
```
4.Clone or download this repository to your local machine.

5. Open a terminal and navigate to the directory containing the script.

6. Run the script using the following command:

  ```bash
  Copy code
  sudo python dns_spoof.py
```
Note: You need to run the script with sudo privileges to access the network interface and modify DNS packets.

7. The script will intercept DNS packets and modify responses to redirect traffic to the specified IP address.

## Explanation
This script utilizes netfilterqueue to intercept and modify DNS packets passing through the system. It listens for DNS response packets and modifies them to spoof DNS records for a specific domain. In this example, DNS responses for www.bing.com are spoofed to redirect traffic to the IP address 192.168.43.198.

## Disclaimer
This script is provided for educational purposes only. DNS spoofing is a malicious activity and can have serious consequences if used improperly. Use this script responsibly and only on networks you own or have explicit permission to test.
