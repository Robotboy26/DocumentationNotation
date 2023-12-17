import http.server
import socketserver
import os

base_path = "data/html"  # Replace with the actual base folder path

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        file_path = os.path.join(base_path, self.path[1:])
        if os.path.isfile(file_path):
            if file_path.endswith(".css"):
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        elif os.path.isdir(file_path):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.list_directory(file_path)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"File not found")

    def list_directory(self, path):
        self.wfile.write(b"<html><head><title>Index</title>")
        self.wfile.write(b"<link rel='stylesheet' type='text/css' href='styles.css'>")
        self.wfile.write(b"</head><body>")
        self.wfile.write(b"<h1>Index of " + path.encode() + b"</h1>")
        self.wfile.write(b"<ul>")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                self.wfile.write(b"<li><a href='" + item.encode() + b"/'>" + item.encode() + b"/</a></li>")
            else:
                self.wfile.write(b"<li><a href='" + item.encode() + b"'>" + item.encode() + b"</a></li>")
        self.wfile.write(b"</ul>")
        self.wfile.write(b"</body></html>")

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("Server started on port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Keyboard interrupt received, closing the server.")
            httpd.server_close()

