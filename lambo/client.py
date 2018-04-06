import json
import requests
import lambo.sanitizer


class LamboClient:
    def __init__(self, username, password, authkey=None, host='http://github.sharath.pro', port=80):
        self.username = username
        self.password = password
        self.authkey = authkey
        self.host = host + ':' + str(port)
        self.login()

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

    def pricetime(self, name, n=10):
        data = self.data(name)
        x = []
        y = []
        for i in range(len(data)):
            data[i]['last_updated'] = i + 1
        data.reverse()
        for i in range(len(data)):
            if i < n:
                x.append(data[i]['last_updated'])
                y.append(data[i]['price_usd'])
        return lambo.sanitizer.Sanitizer(x, y).sanitize()
