import os
import http.server
import socketserver

PORT = 8000  # Change this port number if needed

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Set the file to be served
        file_to_serve = "output.html"

        # Check if the file exists in the current directory
        if not os.path.exists(file_to_serve):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")
        else:
            # Serve the file using the SimpleHTTPRequestHandler
            super().do_GET()

def start_webserver(port):
    try:
        # Set up the HTTP server
        handler = MyHttpRequestHandler
        httpd = socketserver.TCPServer(("", port), handler)
        print(f"Server started at http://localhost:{port}")

        # Start the server
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

if __name__ == "__main__":
    start_webserver(PORT)

