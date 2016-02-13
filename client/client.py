import requests
import logging
import argparse


parser = argparse.ArgumentParser('Client usage')
parser.add_argument('frontend', type=str, default='http://localhost:8000', help='URL for instance of Frontend server',
                    metavar='-f')

args = parser.parse_args()

front_url = args.frontend

logpath = r'/hostdata/client.log'
serverdb = r'/hostdata/backend_list.txt'

content = list()
backlist = dict()
key = 'backend{0}'

# Read the "back-end nodes list"
with open(serverdb, 'r', ) as f:
    i = 0
    for line in f:
        backlist[key.format(i)] = line.strip('\n"')
        i += 1

r = requests.post(front_url, data=backlist)

# To prevent log from REQUESTS info messages, we set for logging WARNING level
logging.basicConfig(format='%(levelname)s:%(message)s', filename=logpath, level=logging.WARNING)
logging.warning('Outcoming connection: {0} | has processed with code {1} | Elapsed time: {2}'.format(r.url, r.status_code, r.elapsed))

# Write to end list of backend nodes
with open(logpath, 'a', ) as f:
    for key, value in backlist.items():
        f.write(value)
        f.write("\n")