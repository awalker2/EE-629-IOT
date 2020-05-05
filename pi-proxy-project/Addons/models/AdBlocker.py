import mitmproxy.http
from mitmproxy import ctx

class AdBlocker:   
        def request(self, flow: mitmproxy.http.HTTPFlow):
                x=5
                x=x+1