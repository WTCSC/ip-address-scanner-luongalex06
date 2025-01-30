[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cYbEVSqo)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17932234)

# IP Scanner - The Ultimate Network Explorer
This IP Scanner script is designed to scan a given subnet, ping each host, and report back who's up, who's down, and who might be hiding in the shadows.

With its easy to use Python code, you can:
 - Discover active hosts in your network.

 - Identify devices that are down or unresponsive.

 - Get response times for each reachable IP.

 - Run this script, and feel like a network guru in seconds!

 # Requirements

To run this script, you’ll need:

-  Python 3.x (Tested on Python 3.8+)
- A computer with internet/network access
- Permission to ping the network (Admin rights may be needed)
- The ipaddress module (Pre-installed with Python 3)

# Usage

Running the scanner is super simple! Just open your terminal or command prompt and type:

`python ip_scanner.py <CIDR>`

For example:

`python ip_scanner.py 192.168.1.0/24`

This will scan all possible IPs in the 192.168.1.0/24 subnet and tell you which ones are online, offline, or encountered an error.

# Notes & Warnings 

Only use this script on networks you own or have permission to scan. Always check with your network administrator before running scans.