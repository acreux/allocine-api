#!/usr/bin/env python

"""
Allocine API:
"""

from datetime import datetime
from Crypto.Hash.SHA import SHA1Hash
import requests
import urllib
import base64
from dispatcher import AllocineDispatcher

class Allocine(object):

    def __init__(self):
        self.dispatcher = AllocineDispatcher()

    def search(self, code):
        return self.dispatcher.movie(code)

a = Allocine()
from pprint import pprint
pprint(a.search('128188'))
b = a.search('128188')
pprint(b['movie']['statistics']['userRating'])