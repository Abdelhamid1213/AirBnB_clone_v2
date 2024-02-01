#!/usr/bin/env bash
# This script sets up the web server for the AirBnB clone project.

apt -y update
apt -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

CONFIG=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name malloc.tech www.malloc.tech;
    add_header X-Served-By \$hostname;
    error_page 404 /404.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /404.html {
        root /var/www/html;
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }

    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/watch?v=xvFZjo5PgG0 permanent;
    }
}"

bash -c "echo -e '$CONFIG' > /etc/nginx/sites-enabled/default"

service nginx restart
