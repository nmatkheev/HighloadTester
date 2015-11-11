#!/usr/bin/python3

__author__ = 'lancer'

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
        st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')        # '%Y-%m-%d %H:%M:%S')
        logging.debug('Incoming connection: {0} | time: {1}'.format(self.client_address, st))        # ('127.0.0.1', 64520)   at   14:12:09


parser = argparse.ArgumentParser('backend.py')
parser.add_argument('url',  type=str, help='URL for instance of Backend server', default='localhost', metavar='-u')
parser.add_argument('port', type=int, help='PORT number', default=9000, metavar='-P')
parser.add_argument('inst', type=int, help='Instance number', default=1, metavar='-i')

args = parser.parse_args()

url = args.url
port = args.port
inst = args.inst
logpath = r'/Users/lancer/PycharmProjects/HighloadTester/backend{0}.log'.format(inst)
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.DEBUG)

serv = HTTPServer((url, port), HttpProcessor)
serv.serve_forever()
