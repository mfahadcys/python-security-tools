# Python Security Tools

Small Python scripts I'm building while learning cybersecurity fundamentals — networking, scripting, and basic security concepts.

## Scripts

### `port_scanner.py`
A simple TCP port scanner that checks which ports are open on a given host.

**How it works:**
- Takes a target host and a port range as input
- Attempts a socket connection to each port
- Reports which ports respond as open

**Usage:**
```bash
python port_scanner.py
```
You'll be prompted for a target host and a port range.

**⚠️ Only scan hosts you own or have explicit permission to test.**
Good practice targets: `127.0.0.1` (your own machine) or `scanme.nmap.org` (a legal public test target provided by Nmap).

## What I'm learning here
- How TCP connections work at a basic level
- Python's `socket` module
- Writing small, readable security tools from scratch

More scripts will be added here as I keep learning.
