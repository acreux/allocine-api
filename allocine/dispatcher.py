#!/usr/bin/env python

from datetime import datetime
from Crypto.Hash.SHA import SHA1Hash
import requests
import urllib
from collections import OrderedDict
import base64
from connector import AllocineConnector

class AllocineDispatcher(object):

    def __init__(self):
        self.connector = AllocineConnector()
        self.api_partner = "100043982026"

        self.global_param =  {'partner': self.api_partner, 'format': 'json'}
    
    def _dispatch(api_method):

        presets = {
            'movielist': { 'profile': 'large' },
            'movie': { },
            'tvserieslist': { 'filter': 'top', 'order': 'viewcount' },
            'tvseries': { 'profile': 'large' },
            'tvseriesbroadcastlist': { 'profile': 'large' },
            'season': { 'profile': 'large' },
            'seasonlist': { 'profile': 'small' },
            'news': { 'profile': 'large' },
            'newslist': { 'profile': 'large' },
            'media': { 'mediafmt': 'mp4' },
            'feature': { 'profile': 'large' },
            'featurelist': { 'profile': 'large' },
            'picturelist': { 'profile': 'large' },
            'videolist': { 'mediafmt': 'mp4' },
            'search': { 'filter': 'movie,tvseries,theater,news,video' }
        }

    def search(self, q, format='json', filter='', count=20):
        pass

    def movie(self, code, profile='large', filter=''):
        params = self.global_param.copy()
        params.update({'code': code,
                       'profile': profile})
        return self.connector.get('movie', params)
