Network Security Basics


-->Firewalls:

>>Definition:
A firewall is a security barrier that monitors and filters network traffic. 
It acts as a gatekeeper between a trusted internal network (like your home or office) 
and untrusted external networks (like the internet).

>>Functions:
-Packet filtering > allows or blocks packets based on rules (e.g., IP address, port, protocol).
-Stateful inspection > tracks the state of connections (open/established/closed).
-Proxying > acts as a middleman between clients and servers.
-Logging & alerts > records suspicious activity.

>>Types:
-Network-based Firewalls → Protects entire networks (hardware devices).
-Host-based Firewalls → Installed on individual devices (e.g., Windows Firewall).
-Next-Gen Firewalls (NGFWs) → Add features like intrusion detection and application filtering.

>>Example Command:
sudo ufw status
sudo ufw enable                 # Enable firewall
sudo ufw allow 443/tcp          # Allow HTTPS traffic
sudo ufw deny 23/tcp            # Block Telnet (unsafe)



-->Virtual Private Networks

>>Definition:
A VPN creates a secure, encrypted tunnel between your device and a remote server.

>>How it Works:
-Encrypts all your internet traffic.
-Replaces your IP address with the VPN server’s IP.
-Secures traffic on public Wi-Fi networks.

>>Protocols Used:
-OpenVPN – open-source, secure.
-IKEv2/IPSec – fast, good for mobile devices.
-WireGuard – modern, lightweight, highly secure



-->Hypertext Transfer Protocol Secure


>>Definition:
HTTPS is the secure version of HTTP. 
It uses SSL/TLS certificates to encrypt communication between a web browser and a server.

>>How It Works:
-Browser connects to website.
-Server provides its SSL/TLS certificate.
-Browser verifies it with a Certificate Authority (CA).
-If valid → connection is encrypted with session keys.



-->Port Scanning


>>Definition:
A port scan checks which network ports are open, closed, or filtered on a target device.

>>Common Port States:
-Open > Service is accepting connections.
-Closed > No service is listening, but system is reachable.
-Filtered > Firewall is blocking access (can’t confirm).

>>Common Tools
-Nmap (Network Mapper) : Most popular scanning tool.
-Netcat : Lightweight tool for testing connections.
-Zenmap : GUI version of Nmap.

>>Nmap Examples
nmap 192.168.1.1               # Scan a local router
nmap -F scanme.nmap.org        # Fast scan common ports
nmap -A scanme.nmap.org        # Deep scan with OS detection



