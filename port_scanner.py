"""
Simple Port Scanner
--------------------
Scans a target host for open TCP ports within a given range.

Usage:
    python port_scanner.py

This is an educational tool — only scan hosts you own or have
explicit permission to test.
"""

import socket
from datetime import datetime


def scan_port(target: str, port: int, timeout: float = 0.5) -> bool:
    """Try to connect to a single port. Returns True if it's open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target, port))
        return result == 0  # 0 means the connection succeeded
    finally:
        sock.close()


def scan_range(target: str, start_port: int, end_port: int) -> list[int]:
    """Scan a range of ports and return the list of open ones."""
    open_ports = []
    print(f"Starting scan on {target} ({start_port}-{end_port})")
    print(f"Time started: {datetime.now()}\n")

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"  [OPEN] Port {port}")
            open_ports.append(port)

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")
    return open_ports


if __name__ == "__main__":
    target_host = input("Enter target host (e.g. scanme.nmap.org or 127.0.0.1): ").strip()
    start = int(input("Start port (e.g. 20): ").strip())
    end = int(input("End port (e.g. 100): ").strip())

    scan_range(target_host, start, end)
