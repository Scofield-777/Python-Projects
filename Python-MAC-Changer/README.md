# MAC Address Changer

This Python script allows you to change the MAC (Media Access Control) address of a network interface on your system.

## Prerequisites

- Python 2.x
- Linux-based operating system (tested on Ubuntu)

## Usage

1. Make sure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the directory containing the script.
4. Run the script using the following command:

   ```bash
   python mac_changer.py -i <interface> -m <new_mac_address>
Replace <interface> with the name of the network interface you want to change (e.g., eth0, wlan0) and <new_mac_address> with the desired MAC address.

## Options
-i, --interface: Specify the network interface for which you want to change the MAC address.
-m, --mac: Specify the new MAC address you want to assign to the interface.

## Example
Change the MAC address of the interface named eth0 to 00:11:22:33:44:55:

  ```bash
  Copy code
  python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```
### Disclaimer
This script is provided for educational purposes only. Changing MAC addresses without proper authorization may violate the terms of service of your network provider or be illegal in your jurisdiction. Use it responsibly and at your own risk.
