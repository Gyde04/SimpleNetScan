#!/usr/bin/env python3

import json
from datetime import datetime

class ScanReport:
    def __init__(self, scan_results):
        self.results = scan_results
        self.timestamp = datetime.now()

    def generate_text_report(self):
        """Generate a plain text report"""
        report = []
        report.append("Network Security Scan Report")
        report.append(f"Generated: {self.timestamp}\n")

        for host, data in self.results.items():
            report.append(f"Host: {host}")
            report.append(f"State: {data.get('state', 'unknown')}\n")

            if 'osmatch' in data:
                report.append("Operating System Detection:")
                for os in data['osmatch']:
                    report.append(f"- {os['name']} (Accuracy: {os['accuracy']}%)")
                report.append("")

            for proto in data.get('protocols', []):
                report.append(f"Protocol: {proto}")
                ports = data.get('ports', {}).get(proto, {})
                if ports:
                    report.append("Port\tState\tService\tVersion")
                    report.append("-" * 50)
                    for port, info in ports.items():
                        report.append(f"{port}\t{info['state']}\t{info['service']}\t{info['version']}")
                else:
                    report.append("No open ports found")
                report.append("")

        return "\n".join(report)

    def generate_html_report(self):
        """Generate an HTML report"""
        html = []
        html.append("<!DOCTYPE html>")
        html.append("<html><head>")
        html.append("<style>")
        html.append("body { font-family: Arial, sans-serif; margin: 20px; }")
        html.append("table { border-collapse: collapse; width: 100%; }")
        html.append("th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }")
        html.append("th { background-color: #f2f2f2; }")
        html.append("</style>")
        html.append("</head><body>")
        
        html.append("<h1>Network Security Scan Report</h1>")
        html.append(f"<p>Generated: {self.timestamp}</p>")

        for host, data in self.results.items():
            html.append(f"<h2>Host: {host}</h2>")
            html.append(f"<p>State: {data.get('state', 'unknown')}</p>")

            if 'osmatch' in data:
                html.append("<h3>Operating System Detection:</h3>")
                html.append("<ul>")
                for os in data['osmatch']:
                    html.append(f"<li>{os['name']} (Accuracy: {os['accuracy']}%)</li>")
                html.append("</ul>")

            for proto in data.get('protocols', []):
                html.append(f"<h3>Protocol: {proto}</h3>")
                ports = data.get('ports', {}).get(proto, {})
                if ports:
                    html.append("<table>")
                    html.append("<tr><th>Port</th><th>State</th><th>Service</th><th>Version</th></tr>")
                    for port, info in ports.items():
                        html.append(f"<tr><td>{port}</td><td>{info['state']}</td>"
                                  f"<td>{info['service']}</td><td>{info['version']}</td></tr>")
                    html.append("</table>")
                else:
                    html.append("<p>No open ports found</p>")

        html.append("</body></html>")
        return "\n".join(html)

    def save_report(self, filename, report_type='text'):
        """Save the report to a file"""
        if report_type == 'html':
            content = self.generate_html_report()
            extension = 'html'
        else:
            content = self.generate_text_report()
            extension = 'txt'

        output_file = f"{filename}.{extension}"
        with open(output_file, 'w') as f:
            f.write(content)
        return output_file
