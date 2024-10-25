# SimpleNetScan

## Overview
SimpleNetScan is a comprehensive network security scanning tool built in Python that demonstrates various cybersecurity concepts. This tool is designed for security professionals and enthusiasts to perform network reconnaissance and security assessments in a controlled, authorized environment.

## 🚀 Features

### Multiple Scan Types
- **Basic Scan**: Standard port and service detection
- **Aggressive Scan**: Comprehensive scanning with OS detection
- **Stealth Scan**: Slower, less detectable scanning
- **Comprehensive Scan**: Full-range analysis with script scanning

### Core Capabilities
- 🔍 Port scanning with service detection
- 🖥️ Operating System detection and fingerprinting
- 📊 Detailed service version identification
- 📝 Comprehensive reporting system
- 🎯 Customizable scan parameters

### Reporting Features
- Text-based reports for command-line viewing
- HTML reports for better visualization
- CSV output for data analysis
- Detailed timestamps and scan information

## 📋 Prerequisites

### System Requirements
- Python 3.7 or higher
- Nmap 7.80 or higher
- Root/Administrator privileges (for advanced scan types)

### Operating System Support
- macOS
- Linux
- Windows (with limitations)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Gyde04/SimpleNetScan.git
cd SimpleNetScan
```
### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
```bash

# On macOS/Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
```
### 3. Install Dependencies
```bash
**pip install -r requirements.txt
```
4. Install Nmap

macOS: brew install nmap
Linux: sudo apt-get install nmap
Windows: Download from nmap.org

💻 Usage
Basic Scan
```bash
sudo python3 simple_netscan.py 127.0.0.1
```
Advanced Usage
```bash
sudo python3 simple_netscan.py [target_ip] -p [port_range] -t [scan_type] -o [output_file]
```
