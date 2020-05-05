from mitmproxy import ctx, http
from tinydb import TinyDB, Query

class JSONLogger:
        def __init__(self):
            # Setup the database, will create new one if none exist
            self.db = TinyDB('Data/db.json')

        # Only concenred with logging HTTP responses for now
        def response(self, flow: http.HTTPFlow) -> None:
                host = flow.response.pretty_host
                httpVer = flow.response.http_version
                size = len(flow.response.content)

                # Insert the info about the host into the database
                self.db.insert(
                    {'host': str(host), 'httpVer': str(httpVer), 'size': str(size)}
                )