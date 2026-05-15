import subprocess
import ipaddress
import socket
import os
import requests
import re


def ping_host(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", "-n", "-W", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except Exception:
        return False


def scan_network_ping(network):
    print(f"Scanning network {network} using ping...")
    live_hosts = []
    for ip in ipaddress.IPv4Network(network, strict=False):
        if ping_host(str(ip)):
            print(f"Host {ip} is UP")
            live_hosts.append(str(ip))
    return live_hosts


def scan_ports(host, start_port=1, end_port=1025, timeout=1):
    print(f"Scanning ports on host {host}...")
    open_ports = []
    for port in range(start_port, end_port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                if s.connect_ex((host, port)) == 0:
                    print(f"Port {port} is OPEN on {host}")
                    open_ports.append(port)
        except Exception:
            pass
    return open_ports


def run_nmap(host, ports):
    ports_str = ",".join(map(str, ports))
    print(f"Running Nmap on {host} with ports: {ports_str}...")
    command = f"nmap -sV --script=vuln {host} -p {ports_str} "
    os.system(command)

def run_nikto(host, port):
    print(f"Running Nikto on {host}:{port}...")
    command = f"nikto -h {host}:{port}"
    os.system(command)

def get_email_http(host, port):
    print(f"Searching for emails on {host}:{port}...")
    try:
        url = f"http://{host}:{port}"
        response = requests.get(url)
        html = response.text
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = re.findall(regex, html)
        uniqe_emails = sorted(set(emails))
        print(f"emails found: {uniqe_emails}")
        return uniqe_emails

    except requests.exceptions.RequestException as e:
        print(f"Error getting page from {host}:{port}:{e}")
        return []

def get_email_https(host, port):
    print(f"Searching for emails on {host}:{port}...")
    try:
        url = f"https://{host}:{port}"
        response = requests.get(url)
        html = response.text
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = re.findall(regex, html)
        uniqe_emails = sorted(set(emails))
        print(f"emails found: {uniqe_emails}")
        return uniqe_emails

    except requests.exceptions.RequestException as e:
        print(f"Error getting page from {host}:{port}:{e}")
        return []

def main():
    network = input("Enter network in Range (e.x., 10.0.2.0/24): ")
    live_hosts = scan_network_ping(network)

    for host in live_hosts:
        open_ports = scan_ports(host)

        if open_ports:
            run_nmap(host, open_ports)
            if 80 in open_ports:
                run_nikto(host, 80)
                get_email_http(host, 80)
            if 8080 in open_ports:
                run_nikto(host, 8080)
                get_email_http(host, 8080)
            if 443 in open_ports:
                run_nikto(host, 443)
                get_email_https(host, 443)

if __name__ == "__main__":
    main()
