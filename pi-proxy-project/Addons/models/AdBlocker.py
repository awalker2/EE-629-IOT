import mitmproxy.http
from mitmproxy import ctx

class AdBlocker:   
        def __init__(self):
               self.blockedHostnames = ["pagead2.googlesyndication.com"]

        def request(self, flow: mitmproxy.http.HTTPFlow):
                host = flow.request.host
                if host in self.blockedHostnames:
                        print("Blocked request to: " + host)
                        flow.kill()

