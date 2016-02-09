'''
Created on Dec 4, 2012

@author: boatkrap
'''


from PyQt5.QtCore import QUrl

class MatchDict(dict):
    def getlist(self, name):
        return [self.get(name)]

class ResourceContext:
    def __init__(self, config, session, apmn_client=None):
        ''''''
        self.config = config
        self.matchdict = MatchDict()
        self.session = session
        self.apmn_client = apmn_client

    def route_url(self, name):
        return self.route_path(name)

    def route_path(self, name):
        route = self.config.get_route(name)
        if route:
            return route['url']

        return None

    def redirect_url(self, name):
        return QUrl(self.route_path(name))

    def add_args(self, args):
        if args is not None:
            self.matchdict.update(args)

    def remember(self, user):
        self.session['user']=user

    def forget(self):
        del self.session['user']
