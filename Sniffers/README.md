# HTTP Packet Sniffer

This Python script allows you to sniff HTTP packets on a specified network interface and extract URLs and potential login information.

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
  sudo python http_sniffer.py
```
Note: You need to run the script with sudo privileges to access the network interface and capture HTTP packets.

6. The script will start sniffing HTTP packets on the specified network interface (wlan0 by default).

## Explanation
This script utilizes Scapy to sniff HTTP packets on the specified network interface. It listens for HTTP request packets and extracts URLs and potential login information from the packet payload. The extracted information is then printed to the console for analysis.

## Disclaimer
This script is provided for educational purposes only. Sniffing HTTP packets can be considered intrusive and may violate the terms of service of your network provider or be illegal in your jurisdiction. Use this script responsibly and only on networks you own or have explicit permission to monitor.
