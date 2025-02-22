# 🚀 Multithreaded Port Scanner

## 📌 Description
This is a fast and efficient multithreaded port scanner written in Python. It allows users to scan an IP address or domain name for open ports (1-1024). The script leverages multithreading for speed and efficiency.

## ⚡ Features
- Scans up to **1024** ports quickly using **multithreading**.
- Supports both **IP addresses** and **domain names**.
- Handles errors gracefully, including invalid inputs and network failures.
- Uses a **queue-based threading system** for efficient scanning.

## 🔧 Requirements
- Python 3.x
- A working internet connection (for domain resolution)

## 🛠 Installation & Usage
### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/yourrepo/port-scanner.git
$ cd port-scanner
```

### 2️⃣ Run the Script
```sh
$ python3 port_scanner.py
```

### 3️⃣ Choose a Target
- Enter `1` to scan an **IP Address**.
- Enter `2` to scan a **Domain Name**.

### 4️⃣ View Results
- Open ports will be displayed in the terminal.
- If no open ports are found, the script will inform you.

## 📜 Example Output
```
Enter choice
 1. IP ADDRESS
 2. DOMAIN NAME
2
ENTER A DOMAIN NAME: example.com
Resolved Domain example.com to IP: 93.184.216.34

[+] Scanning target 93.184.216.34...

PORT 80 IS OPEN LESSFUCKING GOOO!!
PORT 443 IS OPEN LESSFUCKING GOOO!!

🔥🔥 OPEN PORTS 🔥🔥
👉 PORT 80 IS OPEN
👉 PORT 443 IS OPEN
```

## ⚠️ Disclaimer
This script is intended for **educational and authorized security testing purposes only**. Unauthorized scanning of networks that you do not own or have explicit permission to scan may be illegal.

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the script's efficiency or add new features.

## 📜 License
This project is open-source and available under the **MIT License**.

---


