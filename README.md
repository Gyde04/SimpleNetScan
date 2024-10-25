---

# SimpleNetScan

## Overview
**SimpleNetScan** is a powerful network security scanning tool built in Python, ideal for security professionals and enthusiasts. It facilitates network reconnaissance and security assessments in a controlled, authorized environment, showcasing various cybersecurity concepts.

---

## 🚀 Features

### Multiple Scan Types
- **Basic Scan**: Standard port and service detection.
- **Aggressive Scan**: Comprehensive scanning with OS detection.
- **Stealth Scan**: Slower, less detectable scanning.
- **Comprehensive Scan**: Full-range analysis with script scanning.

### Core Capabilities
- 🔍 **Port Scanning with Service Detection**
- 🖥️ **Operating System Detection and Fingerprinting**
- 📊 **Detailed Service Version Identification**
- 📝 **Comprehensive Reporting System**
- 🎯 **Customizable Scan Parameters**

### Reporting Features
- **Text-Based Reports**: Easy command-line viewing.
- **HTML Reports**: Enhanced visualization for reporting.
- **CSV Export**: Ideal for data analysis.
- **Detailed Timestamps and Scan Information**: Log and track scanning details.

---

## 📋 Prerequisites

### System Requirements
- **Python** 3.7 or higher
- **Nmap** 7.80 or higher
- **Root/Administrator Privileges** (for advanced scan types)

### Supported Operating Systems
- **macOS**
- **Linux**
- **Windows** (with some limitations)

---

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Gyde04/SimpleNetScan.git
   cd SimpleNetScan
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Nmap**
   - macOS: `brew install nmap`
   - Linux: `sudo apt-get install nmap`
   - Windows: Download from [nmap.org](https://nmap.org/)

---

## 💻 Usage

### Basic Scan
```bash
sudo python3 simple_netscan.py 127.0.0.1
```

### Advanced Usage
```bash
sudo python3 simple_netscan.py [target_ip] -p [port_range] -t [scan_type] -o [output_file]
```

### Command-Line Options

| Option       | Description                             | Example                       |
|--------------|-----------------------------------------|-------------------------------|
| `-p`, `--ports` | Port range to scan                    | `-p 1-1000`                   |
| `-t`, `--type`  | Scan type (basic/aggressive/stealth/comprehensive) | `-t aggressive`             |
| `-o`, `--output` | Output file name                    | `-o scan_results`             |

### Example Commands
```bash
# Basic scan of localhost
sudo python3 simple_netscan.py 127.0.0.1

# Aggressive scan of specific ports
sudo python3 simple_netscan.py 192.168.1.1 -p 20-100 -t aggressive

# Comprehensive scan with HTML output
sudo python3 simple_netscan.py 10.0.0.1 -t comprehensive -o network_audit
```

---

## 📊 Output Examples

### Text Output
```bash
Host: 192.168.1.1
State: up
Ports:
80/tcp   open  http
443/tcp  open  https
...
```

### HTML Report
Generates a formatted HTML file with:
- Scan summary
- Detailed port listings
- Service information
- OS detection results

---

## 🔒 Security Considerations

### Important Notes
- Only scan networks you own or have explicit permission to test.
- Some scan types may trigger security systems.
- Use stealth scan options when network impact is a concern.

### Best Practices
- Obtain written permission before scanning.
- Document all scanning activities.
- Review logs for unexpected behavior.
- Follow responsible disclosure practices.

---

## 🤝 Contributing
We welcome contributions! Please follow these steps:
1. **Fork** the repository.
2. Create a **feature branch**.
3. **Commit** your changes.
4. **Push** to your fork.
5. Submit a **pull request**.

--- 
