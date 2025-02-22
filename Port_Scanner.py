# STEP 1. IMPORTING MODULES
import ipaddress
import re
import sys
import socket
import threading  # 🚀 NEW: Multithreading for speed

# Function to validate domain format
def valid_domain(domain):
    pattern = r"^(?!-)[A-Za-z0-9.-]{1,253}(?<!-)\.[A-Za-z]{2,6}$"
    return bool(re.match(pattern, domain))

# Function to scan a single port
def scanning_port(IP, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((IP, port))

        if result == 0:
            print(f"PORT {port} IS OPEN LESSFUCKING GOOO!!")
            open_ports.append(port)  # Store open ports in a list
        
        s.close()
    except socket.error:
        pass  # No need to print connection errors for every closed port
    except KeyboardInterrupt:
        print("\nSTOP FUCKING WITH YOUR KEYBOARD")
        sys.exit()

# STEP 2. DEFINING THE TARGET
IP = None  # Initialize IP variable
choice = int(input("Enter choice\n 1. IP ADDRESS\n 2. DOMAIN NAME\n"))

if choice not in (1, 2):
    print("FUCK OFF!! PICK CORRECT CHOICE")
    sys.exit()

if choice == 1:
    IP = input("ENTER IP ADDRESS\n")
    try:
        ip = ipaddress.ip_address(IP)  # Validate IP address
        print(f"Valid IP address: {IP}")
    except ValueError:
        print("YOU FUCKING NOOB THAT'S WRONG")
        sys.exit()

elif choice == 2:
    domain = input("ENTER A DOMAIN NAME: ")
    if valid_domain(domain):
        try:
            IP = socket.gethostbyname(domain)  # Convert domain to IP
            print(f"Resolved Domain {domain} to IP: {IP}")
        except socket.gaierror:
            print("Invalid domain. YOU FUCKING NOOB THAT'S WRONG")
            sys.exit()
    else:
        print("YOU FUCKING NOOB THAT'S WRONG")
        sys.exit()

# Store open ports
open_ports = []

# 🚀 STEP 3. MULTITHREADED PORT SCANNING FUNCTION
def threader():
    while True:
        port = q.get()  # Get a port from the queue
        scanning_port(IP, port)  # Scan the port
        q.task_done()  # Mark task as done

# STEP 4. SET UP THREADING
from queue import Queue

q = Queue()  # Create a queue for ports
num_threads = 50  # 🚀 Adjust this number based on your system (higher = faster)

# Create worker threads
for _ in range(num_threads):
    t = threading.Thread(target=threader)
    t.daemon = True  # Dies when the main program exits
    t.start()

# Put ports into the queue
print(f"\n[+] Scanning target {IP}...\n")
for port in range(1, 1025):  # Scanning ports 1 to 1024
    q.put(port)

# Wait for all threads to finish
q.join()

# STEP 5. PRINT OPEN PORTS
if open_ports:
    print("\n🔥🔥 OPEN PORTS 🔥🔥")
    for port in open_ports:
        print(f"👉 PORT {port} IS OPEN")
else:
    print("\nLMAO NO PORTS ARE OPEN\n")
