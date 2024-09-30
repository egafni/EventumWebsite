
CSS came from: https://github.com/sindresorhus/github-markdown-css
see demo here: https://sindresorhus.com/github-markdown-css/

```
#http
authbind --deep flask  run --port 80 --host 0.0.0.0 --debug

#https
authbind --deep flask  run --port 443 --host 0.0.0.0 --debug
```


openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365


DNS: Just create an A record with the VM's ip

cmds:
sudo usermod -aG google-sudoers egafni
apt-get install rsync dnsutils dig tmux

# this is required to run on port 80/443 without root
sudo apt-get install authbind
sudo touch /etc/authbind/byport/80
sudo chown egafni /etc/authbind/byport/80
sudo chmod 755 /etc/authbind/byport/80

sudo touch /etc/authbind/byport/443
sudo chown egafni /etc/authbind/byport/443
sudo chmod 755 /etc/authbind/byport/443