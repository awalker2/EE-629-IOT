import mitmproxy.http
from mitmproxy import ctx

class JSONLogger:
        def __init__(self):
            self.log = ctx.log

        def request(self, flow: mitmproxy.http.HTTPFlow):
                host = flow.request.pretty_host
                httpVer = flow.request.http_version

                self.log.info("Host: " + host.txt)
                self.log.info("HTTP Ver: " + httpVer)
                