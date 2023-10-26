#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static with nginx
# if ! dpkg -l | grep 'nginx' > /dev/null; then
apt-get update
apt-get install nginx -y
#  Check If nginx is running
  # if ! pgrep nginx > /dev/null; then
service nginx start
#   fi
# fi

root="/data/web_static"
html="<html><head></head><body>Holberton School</body></html>"

# Checks if directories exists before creating them
# if [ ! -d "$root" ]; then
mkdir -p "$root/releases/test"
mkdir -p "$root/shared"
echo "$html" | tee "$root/releases/test/index.html" > /dev/null
# fi
rm -r "$root/current"
ln -sf "$root/releases/test/" "$root/current"
chown -Rh "ubuntu:ubuntu" "/data/"

nginx_cfg_loc="/etc/nginx/sites-available/default"
# if ! grep '/hbnb_static/' "$nginx_cfg_loc" > /dev/null; then
sed -i "/server_name _;/a\\        location /hbnb_static/ {alias $root/current/;}" "$nginx_cfg_loc" > /dev/null
# fi

service nginx restart
