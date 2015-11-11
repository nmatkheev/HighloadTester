#!/usr/bin/python3

__author__ = 'lancer'

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
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')        # '%Y-%m-%d %H:%M:%S')

        logging.warning('Incoming connection: {0} | time: {1}'.format(self.client_address, st))        # ('127.0.0.1', 64520)   at   14:12:09

        for key, value in post_data.items():
            req = requests.get(value[0])
            logging.warning('Outcoming connection: {0} | has processed with code {1} | Elapsed time: {2}'.format(value[0], req.status_code, req.elapsed))


parser = argparse.ArgumentParser('one of the Frontend servers')
parser.add_argument('url', type=str, help='URL for instance of Frontend server')
parser.add_argument('port', type=int, help='PORT number')
parser.add_argument('inst', type=int, help='Instance number')
args = parser.parse_args()

url = args.url
port = args.port
inst = args.inst
logpath = r'/Users/lancer/PycharmProjects/HighloadTester/frontend{0}.log'.format(inst)
# To prevend log from REQUESTS info messages, we set WARNING level
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.WARNING)


serv = HTTPServer(("localhost", 8000), HttpHandler)
serv.serve_forever()

