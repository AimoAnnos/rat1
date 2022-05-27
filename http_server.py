import http.server

HOST_NAME = '172.20.16.61'
PORT_NUMBER = 80

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input('>> ')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(command.encode())

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-Length'])
        postVar = self.rfile.read(length)
        print(postVar.decode())

if __name__ == '__main__':
    server_class = http.server.HTTPServer
    httpd = server_class((HOST_NAME,PORT_NUMBER), MyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
            print('pois pois pois')
            httpd.server_close