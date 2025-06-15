# Scanning Tool 🔍

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Penetration_Testing-orange.svg)

---

## 📚 Description

This **Scanning Tool** is a simple vulnerability scanner and penetration testing script.  
It performs the following operations:

- Pings a target to check if it's up.
- Scans its TCP ports (common or all).
- Detects if port 22 (SSH) is open.
- Performs a simple **bruteforce attack** against the SSH service with a small set of credentials.
- Allows you to connect remotely and execute commands on the compromised machine.

> ⚠️ **This tool is for educational purposes and should only be used on machines you own or have explicit permission to scan. Unauthorized scanning or attacks may be prohibited by law.**  
> Always follow responsible disclosure guidelines.

---

## ⚙️ Requirements

This script is implemented in **Python** (Python 3.x) and utilizes the following libraries:

- [Scapy](https://scapy.net/) for packet scanning
- [Paramiko](http://www.paramiko.org/) for SSH connection

The script will attempt to install missing libraries automatically.  
Make sure you have [Npcap](https://npcap.com) installed (required by Scapy on Windows) and **administrator/root privilege**.

---

## ⚠️ Disclaimer

This tool is for **educational purposes and authorized penetration testing only**.  
Using this tool against targets you do not own or do not have permission to scan is **illegal**.  
The authors do not take responsibility for any unlawful or unintended use.

---

## ❤️ Personal Note

This project was part of my final exam in the Python module during my Cyber Security course.
I'm excited to publish it here and take another step forward in my cybersecurity career!
I’m looking forward to developing my skills further and turning this passion into a profession.

Thank you for checking it out! 🙏
