import nmap
import sys

def scan_network(network):
    scanner = nmap.PortScanner()
    print(f"Scanning network: {network}\n")
    
    # Scan common ports
    scanner.scan(hosts=network, arguments='-p 22,80,443')

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        open_ports = []

        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                if scanner[host][proto][port]['state'] == "open":
                    open_ports.append(port)

        if open_ports:
            print(f"Open Ports: {', '.join(map(str, open_ports))}")
        else:
            print("No monitored ports open")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <network>")
        print("Example: python scanner.py 192.168.1.0/24")
        sys.exit(1)

    scan_network(sys.argv[1])
