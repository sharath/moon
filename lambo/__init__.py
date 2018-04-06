from pymongo import MongoClient
from sshtunnel import SSHTunnelForwarder
from bson.json_util import dumps
import json


class LamboClient:
    def __init__(self, ssh_user, ssh_pass, mongo_host, mongo_port):
        if mongo_host != 'localhost':
            self.tunnel = SSHTunnelForwarder(
                ssh_address_or_host=mongo_host,
                ssh_username=ssh_user,
                ssh_password=ssh_pass,
                remote_bind_address=('127.0.0.1', mongo_port)
            )
            self.tunnel.start()
            self.mongo = MongoClient('127.0.0.1', self.tunnel.local_bind_port)
        else:
            self.mongo = MongoClient(mongo_host, mongo_port)
        self.db = self.mongo['lambo']

    def get_all_data(self):
        qry = self.db.entries.find()
        entries = json.loads(dumps(qry))
        return entries
