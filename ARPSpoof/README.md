# ARP Spoofing Script

This Python script allows you to perform ARP (Address Resolution Protocol) spoofing, a technique used to intercept network traffic between two hosts.

## Prerequisites

- Python 3.x
- Required Python packages: `scapy`

## Usage

1. Make sure you have Python installed on your system.
2. Install the necessary Python package by running:

   ```bash
   pip install scapy

3. Clone or download this repository to your local machine.

4. Open a terminal and navigate to the directory containing the script.

5. Run the script using the following command:

  ```bash
    Copy code
    python arp_spoof.py
  ```
By default, the script is configured to perform ARP spoofing between a target IP address and a gateway IP address. You can customize the target_ip and gateway_ip variables in the script to specify your desired target and gateway IP addresses.

### Explanation
This script works by sending forged ARP packets to the target and gateway, tricking them into thinking that the attacker's machine has the MAC address of the other host. This allows the attacker to intercept and manipulate network traffic between the two hosts.

### Disclaimer
This script is provided for educational purposes only. ARP spoofing attacks can be illegal and unethical if performed without proper authorization. Use this script responsibly and only on networks you own or have explicit permission to test.
