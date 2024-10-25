#!/usr/bin/env python3

import nmap
import sys
from datetime import datetime

def scan_ports(target_ip, port_range):
    nm = nmap.PortScanner()
    print(f"\nScanning target {target_ip}")
    print("Time started:", datetime.now())
    
    try:
        nm.scan(target_ip, port_range, arguments='-sS -sV -T4')
        
        for host in nm.all_hosts():
            print(f"\nHost : {host}")
            print(f"State : {nm[host].state()}")
            
            for proto in nm[host].all_protocols():
                print(f"\nProtocol : {proto}")
                ports = nm[host][proto].keys()
                
                for port in ports:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    print(f"Port : {port}\tState : {state}\tService : {service}")
                    
    except Exception as e:
        print(f"An error occurred: {e}")
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 simple_netscan.py <ip_address>")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    port_range = '1-1024'  # Scanning first 1024 ports
    
    scan_ports(target_ip, port_range)

if __name__ == "__main__":
    main()
