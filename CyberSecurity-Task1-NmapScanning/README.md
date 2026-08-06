

# Task 1 · Basic Network Scanning with Nmap

## What is Nmap?
Nmap (Network Mapper) is an open-source tool used to discover hosts and services 
on a network by sending packets and analyzing responses.

## Why network scanning matters
Scanning identifies open ports, running services, and potential attack surfaces 
on a system — essential for security auditing and vulnerability assessment.

## Findings
- Target: 10.0.2.15 (this Kali VM's own interface, VirtualBox NAT network)
- All 1000 scanned TCP ports returned as filtered (no response)
- OS detection: too many fingerprints matched to identify OS specifically
- This suggests a firewall or NAT configuration is blocking probe packets, 
  which is itself a relevant security observation — a fully filtered host 
  gives an attacker minimal information to work with.

## Ethical use guidelines
Only scan systems you own or have explicit permission to scan. This scan was 
performed entirely on a local VM with no external network scanning.
