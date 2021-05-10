from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import codecs

HOST = '127.0.0.1'
PORT = 6789

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class HttpRequestHandler(BaseHTTPRequestHandler): 
    def do_GET(self):
        print(self.headers)
        print(threading.currentThread().getName())
        self.handle_request()

    def handle_request(self):
        message = ''
        if('index.html' in self.path):
            self.send_response(200)
            message = codecs.open("index.html", 'r')
        else:
            self.send_response(404)
            message = codecs.open("404.html", 'r')
        
        self.send_header('Connection', 'close')
        self.end_headers()

        self.wfile.write(message.read().encode('utf8'))

    def send_response(self, code, message=None):
        self.send_response_only(code, message)
        self.send_header('Server', self.version_string())
        self.send_header('Date', self.date_time_string())

def Main():
    httpServer = ThreadingSimpleServer((HOST, PORT), HttpRequestHandler)

    try:
        httpServer.serve_forever()
    except KeyboardInterrupt:
        pass
    httpServer.server_close()
    print("Parando servidor...")

if __name__ == '__main__':
    Main()