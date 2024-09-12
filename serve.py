#!/usr/bin/env python3
# https://gist.github.com/HaiyangXu/ec88cbdce3cdbac7b8d5
import http.server
import socketserver

PORT = 9876

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
  extensions_map = {
    '': 'application/octet-stream',
    '.manifest': 'text/cache-manifest',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.svg': 'image/svg+xml',
    '.css': 'text/css',
    '.js': 'application/x-javascript',
    '.wasm': 'application/wasm',
    '.json': 'application/json',
    '.xml': 'application/xml',
  }

httpd = socketserver.TCPServer(("localhost", PORT), HttpRequestHandler)

print(f"serving at http://localhost:{PORT}")
httpd.serve_forever()
