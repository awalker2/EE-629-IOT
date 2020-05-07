Goal:
The goal for this project is to run mitmproxy with a few custom Python extensions - one to block ads, and another one to log traffic to JSON. Once a few sites have been visited, a Node server will graph some statistics about the browser traffic run through the proxy. The proxy runs on port 8080, the proxy web interface runs on 9090, and the Node graphs run 9091.

Dependencies:
Python 3.7 - mitmproxy, TinyDB
NodeJS 12 - Chart.JS, express

Running:
    1-Install the dependencies
    2-cd /node_server 
    3-npm install 
    4-cd ..
    5-sudo ./start_proxy.sh

After that, only step 5 is needed, it will start everything

Documentation:
    /node_server - Server to host the graphs based on the JSON, has routes to show graphs and also reset the DB
    /proxy/addons - Where the custom mitmproxy Python addons are loaded from
        /proxy/addons/models/AdBlocker - Blocks ads by hostname or path string match
        /proxy/addons/models/JSONLogger - Stores the web traffic with TinyDB in JSON
    /proxy/data - Where the web traffic is stored as a JSON by TinyDB and accessed by Node
    ./start_proxy.sh - Sets all network settings needed for proxy (will be lost on reboot), starts the proxy with the custom addons, and starts the Node server

