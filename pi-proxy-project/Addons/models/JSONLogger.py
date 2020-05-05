from mitmproxy import ctx, http

class JSONLogger:
        def __init__(self):
            self.log = ctx.log

        def request(self, flow: http.HTTPFlow) -> None:
                host = flow.request.pretty_host
                httpVer = flow.request.http_version

                print(host)
                print(httpVer)
                