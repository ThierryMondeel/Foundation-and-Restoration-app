import http.server
import os

os.chdir('/Users/thierry/Documents/Apps/Foundation-and-Restoration-app')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('', 8787), Handler).serve_forever()
