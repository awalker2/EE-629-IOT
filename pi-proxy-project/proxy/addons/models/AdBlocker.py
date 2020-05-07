import mitmproxy.http
from mitmproxy import ctx

class AdBlocker:   
        def __init__(self):
               # Will block hostnames with these exact matches
               self.blockedHostnames = [
                "pagead2.googlesyndication.com",
                "securepubads.g.doubleclick.net",
                "www.googleadservices.com",
                "ad.doubleclick.net",
                "ade.googlesyndication.com"
               ]
                # Will block paths that contain this
               self.blockedPaths = [
                "/pagead/"
               ]


        def request(self, flow: mitmproxy.http.HTTPFlow):
                blocked = False
                host = flow.request.host
                path = flow.request.path

                # Check blocked hostnames
                if host in self.blockedHostnames:
                        blocked = True
                # Check blocked path substrings
                for blockedPath in self.blockedPaths:
                        if blockedPath in path:
                                blocked = True

                # Drop if blocked
                if (blocked):
                        flow.kill()
                        ctx.log.info("Blocked request to: " + host)

