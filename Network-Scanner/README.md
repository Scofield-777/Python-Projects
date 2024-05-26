# Network Scanner

This Python script allows you to scan a network to discover devices and their corresponding MAC addresses.

## Prerequisites

- Python 2.x
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
  python network_scanner.py -t <target>
  ```
Replace <target> with the IP address or IP range you want to scan. For example, you can specify a single IP address (e.g., 192.168.1.1) or an IP range using CIDR notation (e.g., 192.168.1.1/24).

## Explanation
This script utilizes Scapy, a powerful packet manipulation tool, to send ARP requests to the specified target or IP range. It then listens for ARP responses to identify active devices on the network and extracts their IP and MAC addresses. The results are printed in tabular format for easy readability.

## Example
Scan the IP range 192.168.43.1/24:

  ```bash
  Copy code
  python network_scanner.py -t 192.168.43.1/24
  ```

## Disclaimer
This script is provided for educational purposes only. Network scanning can be considered intrusive and may violate the terms of service of your network provider or be illegal in your jurisdiction. Use this script responsibly and only on networks you own or have explicit permission to scan.
