#!/usr/bin/env python

from datetime import datetime
from Crypto.Hash.SHA import SHA1Hash
import requests
import urllib
from collections import OrderedDict
import base64

class AllocineConnector(object):

    def __init__(self):
        self.api_host_name = 'http://api.allocine.fr'
        self.api_base_path = '/rest/v3/'
        # self.api_partner = 'V2luZG93czg'
        # self.api_secret_key = 'e2b7fd293906435aa5dac4be670e7982'

        self.api_partner = "100043982026"
        self.api_secret_key = "29d185d98c984a359e6e6f26a0474269"
        # self.user_agent = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MSAppHost/1.0)'
        self.user_agent = "Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)"

    def _build_path(self, api_method, params):
        tokens = sorted(['{}={}'.format(urllib.quote(k), urllib.quote(val)) for k, val in params.items()])
        sig = self._sig(tokens)
        return self.api_host_name + self.api_base_path + api_method + '?' + '&'.join(tokens) + '&sed=' + self._sed() + '&sig=' + urllib.quote(sig)

    def _sed(self):
        """
        Return date of today in YYYYMMDD format
        """
        return datetime.now().strftime('%Y%m%d')

    def _sig(self, tokens):
        """
        Return sig parameter base64 encoded

        Hash api_secret_key&param0=p0&param1=p1...&sed=20140510 using SHA1 algorithm
        """
        sig_decoded = self.api_secret_key + '&'.join(tokens) + '&sed={}'.format(self._sed())
        return base64.b64encode(SHA1Hash(sig_decoded).digest())

    def get(self, api_method, params):
        headers = {'User-Agent': self.user_agent}
        req = requests.get(self._build_path(api_method, params), headers=headers)
        try:
            return req.json()
        except ValueError as e:
            print e
            print req.text