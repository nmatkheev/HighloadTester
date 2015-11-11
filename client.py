__author__ = 'lancer'

import requests
import logging


front_url = r'http://localhost:8000'
back_url = r'http://localhost:9000'

logpath = r'/Users/lancer/PycharmProjects/HighloadTester/client.log'

serverdb = r'/Users/lancer/PycharmProjects/HighloadTester/backend_list.txt'

content = list()
backlist = dict()
key = 'backend{0}'

# Read the "back-end servers list"
with open(serverdb, 'r', ) as f:
    i = 0
    for line in f:
        backlist[key.format(i)] = line.strip('\n"')
        i += 1

r = requests.post(front_url, data=backlist)
# r = requests.get(back_url)

# To prevend log from REQUESTS info messages, we set WARNING level
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.WARNING)
logging.warning('Outcoming connection: {0} | has processed with code {1} | Elapsed time: {2}'.format(r.url, r.status_code, r.elapsed))