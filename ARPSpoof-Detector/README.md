# ARP Spoofing Detector

This Python script allows you to detect ARP (Address Resolution Protocol) spoofing attacks on a specified network interface.

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
   python arpspoof_detector.py
   ```
By default, the script is configured to sniff packets on the wlan0 interface. You can customize the interface variable in the script to specify your desired network interface.

## Explanation
This script works by using Scapy, a powerful packet manipulation tool, to sniff ARP packets on the specified network interface. It detects ARP spoofing attacks by comparing the source MAC address in ARP replies with the real MAC address of the corresponding IP address. If a discrepancy is detected, indicating a possible ARP spoofing attack, a warning message is printed.

## Disclaimer
This script is provided for educational purposes only. Detecting ARP spoofing attacks can be illegal and unethical if performed without proper authorization. Use this script responsibly and only on networks you own or have explicit permission to test.
