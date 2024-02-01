#!/usr/bin/env bash
#
# This script sets up the web server for the AirBnB clone project.
# It installs Nginx, creates necessary directories, sets up a test HTML file,
# creates a symbolic link, updates the Nginx configuration, and restarts the Nginx service.
# The script should be run with sudo privileges.
#
# Usage: sudo ./0-setup_web_static.sh
#
# Note: Make sure to update the server configuration file if necessary.
#
# Dependencies: Nginx
#
# Exit Codes:
#   0 - Success
#   1 - Script should be run with sudo
#
# Example:
#   sudo ./0-setup_web_static.sh
# 

if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo."
  exit 1
fi

apt -y update
apt -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/server {/a \ \ \ \ location \/hbnb_static {\n\ \ \ \ \ \ alias \/data\/web_static\/current\/;\n\ \ \ \ \ \ index index.html;\n\ \ \ \ }\n' /etc/nginx/sites-available/default
service nginx restart
