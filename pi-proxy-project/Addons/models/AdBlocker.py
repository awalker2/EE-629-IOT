import mitmproxy.http
from mitmproxy import ctx

class AdBlocker:   
        def __init__(self):
               self.blockedHostnames = [
                "pagead2.googlesyndication.com",
               "securepubads.g.doubleclick.net"
               ]


        def request(self, flow: mitmproxy.http.HTTPFlow):
                host = flow.request.host
                ctx.log.info("Checking: " + host)
                if host in self.blockedHostnames:
                        ctx.log.info("Blocked request to: " + host)
                        flow.kill()

