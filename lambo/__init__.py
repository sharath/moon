import json

import requests


class LamboClient:
    def __init__(self, username, password, authkey=None, host='http://github.sharath.pro', port=80):
        self.username = username
        self.password = password
        self.authkey = authkey
        self.host = host + ':' + str(port)

    def register(self):
        payload = {'username': self.username, 'password': self.password}
        resp = requests.post(self.host + '/register', data=payload)
        if resp.status_code == 200:
            self.authkey = json.loads(resp.text)['auth_key']
            return self.authkey
        return self.login()

    def login(self):
        payload = {'username': self.username, 'password': self.password}
        resp = requests.post(self.host + '/login', data=payload)
        if resp.status_code == 200:
            self.authkey = json.loads(resp.text)['auth_key']
            return self.authkey
        raise UserWarning('invalid credentials')

    def data(self, name):
        header = {'Authkey': self.authkey}
        resp = requests.post(self.host + '/hist/' + name, headers=header)
        if resp.status_code == 200:
            data = json.loads(resp.text)
            return data
        return None
