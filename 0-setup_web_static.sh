#!/usr/bin/env bash
#A script to setup and configure a nginx account
apt-get install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello Holberton school i am Toluwaloju Kayode" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu /data/
new_loc="\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "/server_name _;$/a $new_loc" /etc/nginx/sites-available/default
sed -i "/n$/d" /etc/nginx/sites-available/default
nginx -s reload
