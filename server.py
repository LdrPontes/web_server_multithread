from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

HOST = '127.0.0.1'
PORT = 6789

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class HttpRequestHandler(BaseHTTPRequestHandler): 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Connection', 'close')
        self.end_headers()
        message =  threading.currentThread().getName()
        self.wfile.write(message.encode('utf8'))
        return

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