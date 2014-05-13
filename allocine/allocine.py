#!/usr/bin/env python

"""
Allocine API:
"""

from dispatcher import AllocineDispatcher

class Allocine(object):

    def __init__(self):
        self.dispatcher = AllocineDispatcher()

    def movie(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('movie', **u_kwargs)

    def search(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['q'] = q
        return self.dispatcher.dispatch('search', **u_kwargs)

    def search_movie(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['filter'] = 'movie'
        return self.search(q, **u_kwargs)

    def search_theater(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['filter'] = 'theater'
        return self.search(q, **u_kwargs)

    def search_person(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['filter'] = 'person'
        return self.search(q, **u_kwargs)

    def search_news(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['filter'] = 'news'
        return self.search(q, **u_kwargs)

    def search_tvseries(self, q, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['filter'] = 'tvseries'
    	return self.search(q, **u_kwargs)

    def reviewlist(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('reviewlist', **u_kwargs)

    def showtimelist(self, **kwargs):
        return self.dispatcher.dispatch('showtimelist', **u_kwargs)

    def media(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('media', **u_kwargs)

    def person(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('person', **u_kwargs)

    def filmography(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('filmography', **u_kwargs)

    def theaterlist(self, **kwargs):
        return self.dispatcher.dispatch('theaterlist', **u_kwargs)

    def tvseries(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('tvseries', **u_kwargs)

    def season(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('season', **u_kwargs)

    def episode(self, code, **kwargs):
        u_kwargs = kwargs.copy()
        u_kwargs['code'] = code
        return self.dispatcher.dispatch('episode', **u_kwargs)

a = Allocine()
from pprint import pprint
pprint(a.person('194788'))
