from mitmproxy import ctx, http
from tinydb import TinyDB, Query

class JSONLogger:
        def __init__(self):
            # Setup the database, will create new one if none exist
            self.db = TinyDB('Data/db.json')

        # Only concenred with logging HTTP responses for now
        def response(self, flow: http.HTTPFlow) -> None:
                host = str(flow.response.pretty_host)
                httpVer = str(flow.response.http_version)
                size = str(len(flow.response.content))
                time = str(flow.response.timestamp_start)

                # Insert the info about the host into the database
                self.db.insert(
                    {'host': host, 'httpVer': httpVer, 'size': size, 'time': time}
                )