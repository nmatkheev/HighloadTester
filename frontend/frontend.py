#!/usr/bin/python3

from urllib import parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import logging
import argparse
import datetime, time


class HttpHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = parse.parse_qs(self.rfile.read(length).decode('utf-8'))

        self.send_response(200)
        self.end_headers()
        # For extra-precision, I capture time when request was handled, then display it inside log
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

        logging.warning('Incoming connection: {0} | time: {1}'.format(self.client_address, st))
        print('Incoming connection: {0} | time: {1}'.format(self.client_address, st))

        for key, value in post_data.items():
            req = requests.get(value[0])
            print('Outcoming connection: {0} | has processed with code {1} | Elapsed time: {2}'.format(value[0], req.status_code, req.elapsed))
            logging.warning('Outcoming connection: {0} | has processed with code {1} | Elapsed time: {2}'.format(value[0], req.status_code, req.elapsed))

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('content-type', 'text/html')
        self.end_headers()


parser = argparse.ArgumentParser('one of the Frontend servers')
parser.add_argument('url', type=str, default='0.0.0.0', help='URL for instance of Frontend server')
parser.add_argument('port', type=int, help='PORT number', default=8000, metavar='-P')
args = parser.parse_args()

url = args.url
port = args.port

from random import randint
id = randint(0, 50)
logpath = r'/hostdata/frontend_{0}.log'.format(id)
# To prevend log from REQUESTS info messages, we set for logging WARNING level
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.WARNING)


serv = HTTPServer((url, port), HttpHandler)
serv.serve_forever()

