#!/bin/bash
# UFW Firewall Configuration Script
# Task 2 - Basic Firewall Configuration with UFW

sudo apt install ufw -y
sudo ufw enable

# Allow SSH traffic (port 22)
sudo ufw allow ssh

# Deny HTTP traffic (port 80)
sudo ufw deny http

# Allow HTTPS traffic (port 443)
sudo ufw allow https

# Deny port 8080
sudo ufw deny 8080

# Show final status
sudo ufw status verbose
