import http.server
import socketserver
import os
import sys

PORT = 8000
PUBLIC_DIR = "public"

os.chdir(PUBLIC_DIR)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.shutdown()
        sys.exit(0)
