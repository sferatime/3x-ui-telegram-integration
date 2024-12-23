import json

import requests as re


class Integration3x:

    def __init__(self, addr, username, password):
        self.addr = addr
        self.username = username
        self.password = password
        self.session = re.Session()

    def login(self) -> bool:
        try:
            r = self.session.post(self.addr + "/login", data={'username': self.username, 'password': self.password})
        except Exception as err:
            print(err)
            return False
        print(r.cookies)
        return True

    def add_inbound(self):
        data = {
            "up": 0,
            "down": 0,
            "total": 0,
            "remark": "New",
            "enable": True,
            "expiryTime": 0,
            "listen": "",
            "port": 55422,
            "protocol": "vless",
            "settings": "{\"clients\": [{\"id\": \"b86c0cdc-8a02-4da4-8693-72ba27005587\",\"flow\": \"\",\"email\": \"sadsant3wz904\",\"limitIp\": 0,\"totalGB\": 0,\"expiryTime\": 0,\"enable\": true,\"tgId\": \"\",\"subId\": \"rqv5zw1ydutamcp0\",\"reset\": 0}],\"decryption\": \"none\",\"fallbacks\": []}",
            "streamSettings": "{\"network\": \"tcp\",\"security\": \"reality\",\"externalProxy\": [],\"realitySettings\": {\"show\": false,\"xver\": 0,\"dest\": \"yahoo.com:443\",\"serverNames\": [\"yahoo.com\",\"www.yahoo.com\"],\"privateKey\": \"wIc7zBUiTXBGxM7S7wl0nCZ663OAvzTDNqS7-bsxV3A\",\"minClient\": \"\",\"maxClient\": \"\",\"maxTimediff\": 0,\"shortIds\": [\"47595474\",\"7a5e30\",\"810c1efd750030e8\",\"99\",\"9c19c134b8\",\"35fd\",\"2409c639a707b4\",\"c98fc6b39f45\"],\"settings\": {\"publicKey\": \"2UqLjQFhlvLcY7VzaKRotIDQFOgAJe1dYD1njigp9wk\",\"fingerprint\": \"random\",\"serverName\": \"\",\"spiderX\": \"/\"}},\"tcpSettings\": {\"acceptProxyProtocol\": false,\"header\": {\"type\": \"none\"}}}",
            "sniffing": "{\"enabled\": true,\"destOverride\": [\"http\",\"tls\",\"quic\",\"fakedns\"],\"metadataOnly\": false,\"routeOnly\": false}",
            "allocate": "{\"strategy\": \"always\",\"refresh\": 5,\"concurrency\": 3}"
        }
        try:
            r = self.session.post(self.addr + "/panel/api/inbounds/add", data=data)
        except Exception as err:
            print(err)
            return False
        print(r.content)
        return True

    def list_inbound(self):
        try:
            r = self.session.get(self.addr + "/panel/api/inbounds/list")
        except Exception as err:
            print(err)
            return {}
        inbound = json.loads(r.content)
        return inbound["obj"]