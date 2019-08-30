import sys
import os
import urllib

from pymongo import MongoClient, errors

username = os.getenv('USER', '')
password = os.getenv('PASSWORD', '')
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
endpoint = os.getenv('ENDPOINT', 'localhost:27017')

try:
    client = MongoClient(
            'mongodb://%s:%s@%s' % (username, password, endpoint),
            serverSelectionTimeoutMS=10000)
    print(client.server_info())
except errors.ServerSelectionTimeoutError as err:
    print(err)
