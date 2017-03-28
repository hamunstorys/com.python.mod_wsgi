#!/usr/bin/env python

from http import server

class MyHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write("Hello World")

if __name__ == '__main__':
    server = server.HTTPServer(('', 8888), MyHandler)
    print("Started WebServer on port 8888...")
    print("Press ^C to quit WebServer")
    server.serve_forever()