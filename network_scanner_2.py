# OP3N1T SECURITY

from scapy.all import ARP, Ether, srp
import requests
import socket
import time

PURPLE = "\033[95m"
YELLOW = "\033[93m"
RESET = '\033[0m'

print()
print(f"{PURPLE}----- WELCOME TO NETWORK SCANNER ------{RESET}")
print()

target_ip = "192.168.1.1/24"

# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=7, verbose=1)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

# Function to detect common device types based on open ports
def detect_device_type(ip):
    common_ports = {21: 'FTP', 22: 'SSH', 80: 'HTTP', 443: 'HTTPS'}
    open_ports = []

    for port in common_ports.keys():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(common_ports[port])
        sock.close()

    return ', '.join(open_ports) if open_ports else 'Unknown'

# Retry function with exponential backoff
def retry_request(url, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, headers={'User-Agent': 'MyScanner/1.0'})
            if response.status_code == 200:
                return response.text.strip()
        except requests.exceptions.RequestException:
            pass
        # Wait before retrying with exponential backoff (1s, 2s, 4s, etc.)
        time.sleep(2 ** retries)
        retries += 1
    return 'Unknown'

# Replace 'YOUR_API_KEY' with your actual API key from macvendors.com
api_key = 'YOUR_API_KEY'

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    client_info = {'ip': received.psrc, 'mac': received.hwsrc, 'manufacturer': 'Unknown', 'device_type': 'Unknown'}

    # Fetch manufacturer information using macvendors.com API with retry logic
    mac_address = received.hwsrc.replace(':', '')
    url = f'https://api.macvendors.com/{mac_address}'
    client_info['manufacturer'] = retry_request(url)
    
    # Determine the device type based on open ports
    client_info['device_type'] = detect_device_type(client_info['ip'])
    
    clients.append(client_info)

# Print clients with additional details
print()
print(f"{YELLOW}Available devices in the network:{RESET}")
print("IP" + " "*18 + "MAC" + " "*20 + "Device Type" + " "*15 + "Manufacturer")
for client in clients:
    print("{:16}    {:17}        {:12}      {}".format(client['ip'], client['mac'], client['device_type'], client['manufacturer']))

print()
print(f"{PURPLE}---------------- DONE -----------------{RESET}")
print()
