try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


class BoatdRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        super(BoatdRequestHandler, self).__init__(*args, **kwargs)

    def do_GET(self, *args, **kwargs):
        print('Requested', self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'application/JSON')
        self.end_headers()
        self.request.sendall('hi there'.encode())

if __name__ == '__main__':
    httpd = HTTPServer(('', 2222),
        BoatdRequestHandler)
    httpd.serve_forever()
