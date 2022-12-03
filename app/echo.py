import datetime
import http.server
import socketserver
from http import HTTPStatus

PORT = 8080
HOST = '0.0.0.0'
Handler = http.server.SimpleHTTPRequestHandler

class EchoHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send()

    def do_HEAD(self):
        self.send()

    def do_POST(self):
        self.send()

    def do_PUT(self):
        self.send()

    def do_PATCH(self):
        self.send()

    def send(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"<html><head><title>{self.command} {self.path}</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>{datetime.datetime.now().isoformat()} {self.command}: {self.path}</p>", "utf-8"))
        print(f'\n\n\nRequest: {self.command} {self.path}')
        self.wfile.write(bytes(f"<p>Headers: {'<br/>'.join([repr(x) for x in self.headers.items()])}</p>", "utf-8"))
        print('\n'.join([repr(x) for x in self.headers.items()]))
        if (self.command in ['POST', 'PATCH', 'PUT']):
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            self.wfile.write(bytes(f"<br/><br/><pr>data: {data}</pr>", "utf-8"))
            print(f'\nPayload: {data}')
        print('\n\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webServer = http.server.HTTPServer((HOST, PORT), EchoHandler)
    print(f"Server started http://{HOST}:{PORT}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Done.")
