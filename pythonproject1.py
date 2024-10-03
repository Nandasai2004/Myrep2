# app.py
from http.server import simpleHTTPRequestHandler,HTTPServer

PORT = 8000

class MyHandler(simpleHTTPRequestHandler):
    def do_GET(self):
        self.send_responce(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('b Hello,world| This is my python web application.')

httpd = HTTPServer(('',PORT),MyHandler)
print(f'Serving on port {PORT}...')
httpd.serve_forever()

