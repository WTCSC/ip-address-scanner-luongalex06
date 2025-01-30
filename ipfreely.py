import ipaddress
import subprocess
import sys
import time

def ping_host(ip):
    # Pings an IP and sees if it's up or down
    try:
        start_time = time.time()
        param = '-n' if sys.platform.startswith('win') else '-c'
        result = subprocess.run(["ping", param, "1", "-w", "500", str(ip)], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                text=True)
        end_time = time.time()
        response_time = int((end_time - start_time) * 1000)  # time
        
        if result.returncode == 0:
            return "UP", f"{response_time}ms"
        else:
            return "DOWN", "No response"
    except Exception as e:
        return "ERROR", str(e)

def scan_network(cidr):
    # Scans the network and pings all hosts
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        print(f"Scanning {cidr}...\n")
        
        up_count, down_count, error_count = 0, 0, 0
        
        for host in network.hosts():
            status, message = ping_host(host)
            print(f"{host} - {status} ({message})")
            
            if status == "UP":
                up_count += 1
            elif status == "DOWN":
                down_count += 1
            else:
                error_count += 1
        
        print("\nScan done.")
        print(f"{up_count} active, {down_count} down, {error_count} errors.")
        
    except ValueError:
        print("Invalid CIDR. Use something like 192.168.1.0/24.")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ip_scanner.py <CIDR>")
    else:
        scan_network(sys.argv[1])
