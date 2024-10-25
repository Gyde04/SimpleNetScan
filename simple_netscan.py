#!/usr/bin/env python3

import nmap
import sys
import os
import argparse
from datetime import datetime
from subprocess import run, PIPE

class NetworkScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()
        
    def check_nmap_installation(self):
        """Check if nmap is installed"""
        try:
            result = run(['which', 'nmap'], stdout=PIPE, stderr=PIPE)
            if result.returncode != 0:
                print("Error: nmap is not installed!")
                print("Please install nmap using: brew install nmap")
                sys.exit(1)
        except Exception as e:
            print(f"Error checking nmap installation: {e}")
            sys.exit(1)

    def scan_ports(self, target_ip, port_range, scan_type='basic'):
        """Scan ports on target IP"""
        print(f"\nScanning target {target_ip}")
        print("Time started:", datetime.now())
        print(f"Scan type: {scan_type}")
        
        try:
            # Different scan types
            scan_types = {
                'basic': '-sV -T4 -A -v',
                'aggressive': '-sS -sV -T4 -A -O -v',
                'stealth': '-sS -T2 -f -v',
                'comprehensive': '-sS -sV -T4 -A -O -v --script=default'
            }
            
            scan_args = scan_types.get(scan_type, scan_types['basic'])
            
            print("Scanning in progress... This may take a few moments.")
            print(f"Scanning ports {port_range}")
            
            self.scanner.scan(target_ip, port_range, arguments=scan_args)
            
            self._print_scan_results(target_ip)
            
        except Exception as e:
            print(f"An error occurred during scanning: {e}")
            if os.geteuid() != 0:
                print("\nNote: Some scan types require root privileges. Try running with sudo.")
    
    def _print_scan_results(self, target_ip):
        """Print formatted scan results"""
        if target_ip not in self.scanner.all_hosts():
            print("No hosts found")
            return
            
        for host in self.scanner.all_hosts():
            print(f"\nHost : {host}")
            print(f"State : {self.scanner[host].state()}")
            
            # OS Detection
            if 'osmatch' in self.scanner[host]:
                print("\nOS Detection:")
                for osmatch in self.scanner[host]['osmatch']:
                    print(f"OS Match: {osmatch['name']} - Accuracy: {osmatch['accuracy']}%")
            
            # Port Scanning Results
            for proto in self.scanner[host].all_protocols():
                print(f"\nProtocol : {proto}")
                ports = sorted(self.scanner[host][proto].keys())
                
                if not ports:
                    print("No open ports found")
                else:
                    print("\nPort\tState\t\tService\t\tVersion")
                    print("-" * 60)
                    
                    for port in ports:
                        state = self.scanner[host][proto][port]['state']
                        service = self.scanner[host][proto][port]['name']
                        version = self.scanner[host][proto][port].get('version', '')
                        product = self.scanner[host][proto][port].get('product', '')
                        
                        print(f"{port}\t{state}\t\t{service}\t\t{product} {version}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='Network Security Scanner')
    parser.add_argument('target', help='Target IP address to scan')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range to scan (default: 1-1000)')
    parser.add_argument('-t', '--type', choices=['basic', 'aggressive', 'stealth', 'comprehensive'],
                        default='basic', help='Type of scan to perform')
    parser.add_argument('-o', '--output', help='Output results to a file')
    
    args = parser.parse_args()
    
    scanner = NetworkScanner()
    scanner.check_nmap_installation()
    
    # Perform the scan
    scanner.scan_ports(args.target, args.ports, args.type)
    
    # Save results if output file specified
    if args.output:
        with open(args.output, 'w') as f:
            f.write(f"Scan Results for {args.target}\n")
            f.write(f"Time: {datetime.now()}\n")
            f.write(f"Scan Type: {args.type}\n")
            f.write(f"Port Range: {args.ports}\n\n")
            f.write(scanner.scanner.csv())

    print("\nScan completed!")
    print("Time finished:", datetime.now())

if __name__ == "__main__":
    main()
