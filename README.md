# WiFi Connected User Finder

## Introduction
WiFi Connected User Finder is a Python script designed to scan a local network and identify active hosts, particularly those connected to the same WiFi network as the host machine. It utilizes ARP scanning techniques to discover active IP addresses within a specified IP range.

## Features
- Discovers active hosts within the local network.
- Identifies users connected to the same WiFi network.
- Supports custom IP address input for flexibility.
- Colorful console output for better visualization.
- Utilizes multithreading for faster scanning.

## Prerequisites
- Python 3.x
- Python libraries: `scapy`, `argparse`, `socket`

## Installation
1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/Cyber-Programer/wifi-users-ip
    ```
3. Install the required Python libraries:
    ```bash
    pip install scapy
    ```
4. Ensure that the `scapy` library is properly installed and configured on your system.

## Usage
1. Navigate to the directory containing the Python script.
   ```bash
    cd wifi-users-ip
   ```
3. Run the script using Python:
    ```bash
    python main.py
    ```
4. Optionally, specify a custom IP address using the `-ip` flag:
    ```bash
    python main.py -ip <custom_wifi_ip_address>
    ```
5. View the console output to see active hosts and connected users within the network.

## Example
To scan the network with a custom IP address:
```bash
python main.py -ip 192.168.10.1
