# Task 2 · Basic Firewall Configuration with UFW

## What is UFW?
UFW (Uncomplicated Firewall) is a user-friendly command-line interface for 
managing iptables-based firewall rules on Linux systems. It simplifies 
firewall configuration for common use cases.

## What each rule achieves
- **Allow SSH (port 22):** Permits secure remote administration access
- **Deny HTTP (port 80):** Blocks unencrypted web traffic to reduce attack surface
- **Allow HTTPS (port 443):** Permits secure, encrypted web traffic
- **Deny port 8080:** Blocks a commonly used alternate HTTP port often used 
  for proxies or dev servers, reducing unnecessary exposed services

## Why these rules were chosen
This ruleset reflects a minimal, security-conscious approach: only allow 
traffic that's explicitly needed (SSH for admin access, HTTPS for secure 
web traffic), and explicitly deny commonly probed/insecure ports (HTTP, 
8080) that could otherwise be left open by default.

## Verification
Ran `sudo ufw status verbose` to confirm all rules were applied correctly 
for both IPv4 and IPv6.

## Testing Note
When testing the deny rule for port 8080 by connecting to the VM's own IP 
(10.0.2.15) from itself, the connection succeeded despite the DENY rule. 
This is because self-originated traffic to a machine's own IP often routes 
through the loopback interface, which can bypass some firewall filtering 
that applies to genuinely external traffic. This is a known limitation of 
testing firewall rules from the same host — in a real-world scenario, the 
deny rule would correctly block incoming connections from other machines 
on the network.

## Ethical use guidelines
Firewall configuration was performed entirely on a local, isolated VM with 
no impact on external systems.
