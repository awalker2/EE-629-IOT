from mitmproxy import ctx

class BasicAddon:
        def __init__(self):
                self.num = 0

        def request(self, flow):
                self.num = self.num + 1
                ctx.log.info("We've seen %d flows" % self.num)

        def response(self, flow):
                if flow.response.headers.get('Content-Type','').startswith("text/html"):
                        flow.response.text = flow.response.text.replace("test", "new word")

addons = [
    BasicAddon()
]
