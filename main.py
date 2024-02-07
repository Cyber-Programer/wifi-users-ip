import platform
import threading
import subprocess
from scapy.all import ARP, Ether, srp
import importlib.util
import argparse
import socket
import sys
from time import sleep as s

class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m000'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
ip_list = []

stdout_lock = threading.Lock()


logo = f'''
           _  __ _
          (_)/ _(_)
 __      ___| |_ _
 \ \ /\ / / |  _| |
  \ V  V /| | | | |
   \_/\_/ |_|_| |_|

    Wifi connected user finder2
                    (2rootv3)
                    
'''

def logo_show():
    animation(logo,colors.YELLOW)

def get_wifi_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        return local_ip
    except socket.error as e:
        animation(f"[-] Socket error:{e}",colors.RED)
        return None

def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

def check_module(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        animation(f"Module '{module_name}' is not installed. Installing...",colors.RED)
        install_module(module_name)
    else:
        # print(f"Module '{module_name}' is already installed.")
        pass

def animation(text,color=colors.RESET):
    with stdout_lock:
        for i in text:
            sys.stdout.write(color + i + colors.RESET)
            sys.stdout.flush()
            s(0.001)
    sys.stdout.write('\n')
    

def check_ip(ip):
    try:
        arg = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', arg, '3', ip]
        subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        
        if wifi_ip == ip:
            print()
            animation(f'[*] Your wifi ip is active : {ip}',colors.MAGENTA)
            print()
        
        else:
            
            animation(f'[~] Host with IP {ip} is online.',colors.GREEN)
            ip_list.append(ip)
    except subprocess.CalledProcessError:
        pass

def scan_ip(base_ip):
    threads = []
    for i in range(1, 256):
        test_ip = f"{base_ip}.{i}"
        # print(test_ip)
        thread = threading.Thread(target=check_ip, args=(test_ip,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def main():
    
    required_modules = ['scapy']
    for module in required_modules:
        check_module(module)
    
    parser = argparse.ArgumentParser(description='Local network scanner')
    parser.add_argument('-ip','--custom-ip',type=str,help='Your wifi Ip address')

    args = parser.parse_args()
    
    logo_show()
    global wifi_ip
    wifi_ip = args.custom_ip if args.custom_ip else '192.168.0.1'
    ip_parts = wifi_ip.split('.')
    base_ip = '.'.join(ip_parts[:-1])
    scan_ip(base_ip)

    print()
    animation(f"Total Users : {len(ip_list)}",colors.YELLOW)
    
    if len(ip_list) == 0:
        animation('Check your wifi ip correct or wrong then try again',colors.RED)
        animation(f'Your wifi ip is : {wifi_ip} if you want to use custome ip then use -ip arg',colors.RED)
        print()
        animation('Example:\npython main.py -ip 192.168.10.1',colors.RED)
if __name__ == '__main__':
    main()
