from mitmproxy import ctx, http
from tinydb import TinyDB, Query

class JSONLogger:
        def __init__(self):
            # Setup the database, will create new one if none exist
            self.db = TinyDB('Data/db.json')

        # Only concenred with logging HTTP responses for now
        def response(self, flow: http.HTTPFlow) -> None:
                host = flow.request.pretty_host
                httpVer = flow.request.http_version
                time = flow.request.timestamp_start

                size = len(flow.response.content)

                # Insert the info about the site into the database
                self.db.insert(
                    {'host': host, 'httpVer': httpVer, 'size': size, 'time': time}
                )