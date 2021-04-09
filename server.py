from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
import json
import time
from message import Message
from upstream import Upstream
import urllib.parse

class Server(BaseHTTPRequestHandler):

    logins = []

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    # GET sends back the object created and sends it upstream
    def do_GET(self):
        self._set_headers()
        # check input here?
        query_param =  urllib.parse.parse_qs(self.path[2:])
        # parse incoming message and choose type of message -- query param returns a list now choosing only 0th element todo: check why
        message = Message(query_param['user'][0],query_param['email'][0])
        # for time being save incoming message in a list here
        self.logins.append(message)
        # send message upstream
        upstream = Upstream(message)
        # return an answer (or just statuscode)
        self.wfile.write(message.toJSON().encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Server, port=8000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...' % port)
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
