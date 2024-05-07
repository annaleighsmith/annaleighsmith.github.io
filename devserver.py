import http.server
import socketserver

PORT = 8000  # You can change this to any available port you prefer


# Define the request handler
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="public", **kwargs)


# Create a socket server
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Serving at port http://localhost:{PORT}")
    # Start the server
    httpd.serve_forever()
