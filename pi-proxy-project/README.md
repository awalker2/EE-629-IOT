Goal:<br />
The goal for this project is to run mitmproxy with a few custom Python extensions - one to block ads, and another one to log traffic to JSON. Once a few sites have been visited, a Node server will graph some statistics about the browser traffic run through the proxy. The proxy runs on port 8080, the proxy web interface runs on 9090, and the Node graphs run on 9091.

Dependencies:<br />
&ensp;Python 3.7 - mitmproxy, TinyDB<br />
&ensp;NodeJS 12 - Chart.JS, express<br />
&ensp;Raspberry Pi 3B+ - ./start_proxy assumes eth0 is desired<br />

Running:<br />
&ensp;1-Install the dependencies<br />
&ensp;2-cd /node_server<br />
&ensp;3-npm install<br />
&ensp;4-npm start<br />
&ensp;6-New terminal - sudo ./start_proxy.sh<br />

Devices can connect by setting their proxy to [Pi IP]:8080 and downloading a certificate from mitm.it

Documentation:<br />
&ensp;/node_server - Server to host the graphs based on the JSON, has routes to show graphs and also reset the DB<br />
&ensp;/proxy/addons - Where the custom mitmproxy Python addons are loaded from<br />
&ensp;&ensp;/proxy/addons/models/AdBlocker - Blocks ads by hostname or path string match, more URLS and paths seemed to partially work for YouTube<br />
&ensp;&ensp;/proxy/addons/models/JSONLogger - Stores the web traffic with TinyDB in JSON<br />
&ensp;/proxy/data - Where the web traffic is stored as a JSON by TinyDB and accessed by Node<br />
&ensp;./start_proxy.sh - Sets all network settings needed for proxy (will be lost on reboot), starts the proxy with the custom addons, and starts the Node server<br />

