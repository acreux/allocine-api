#!/usr/bin/env python

from connector import AllocineConnector

class AllocineDispatcher(object):

    def __init__(self):
        self.connector = AllocineConnector()
        self.api_partner = self.connector.api_partner
        self.global_param = {'partner': self.api_partner, 'format': 'json'}
    
    def dispatch(self, api_method, **kwargs):
        params = self.global_param.copy()
        params.update({key:value for key, value in kwargs.items() if value})
        return self.connector.get(api_method, params)