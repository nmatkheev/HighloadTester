#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import logging, argparse
import datetime, time


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200,'OK')
        self.send_header('content-type','text/html')
        self.end_headers()
        # For extra-precision, I capture time when request was handled, then display it inside log
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        print('Incoming connection: {0} | time: {1}'.format(self.client_address, st))
        logging.debug('Incoming connection: {0} | time: {1}'.format(self.client_address, st))


parser = argparse.ArgumentParser('backend.py')
parser.add_argument('url',  type=str, help='URL for instance of Backend server', default='0.0.0.0', metavar='-u')
parser.add_argument('port', type=int, help='PORT number', default=9000, metavar='-P')

args = parser.parse_args()

url = args.url
port = args.port

# Kostyl
from random import randint
id = randint(0, 50)

logpath = r'/hostdata/backend_{0}.log'.format(id)
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.DEBUG)

serv = HTTPServer((url, port), HttpProcessor)
serv.serve_forever()
