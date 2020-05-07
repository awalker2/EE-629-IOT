sysctl -w net.ipv6.conf.all.forwarding=1

sysctl -w net.ipv4.conf.all.send_redirects=0

iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080
ip6tables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
ip6tables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j REDIRECT --to-port 8080

mitmweb --web-port 9090 --web-host 0.0.0.0 -s ./proxy/addons/load_addons.py
npm start --prefix node_server/
