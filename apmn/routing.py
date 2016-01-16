'''
Created on Dec 3, 2012

@author: superizer
'''
from .views import accounts

def add_route(config):
    config.add_route('index', '/', accounts.login, '/accounts/login.jinja2')
    config.add_route('login', '/login', accounts.login, '/accounts/login.jinja2')
    config.add_route('home', '/home', accounts.home, '/accounts/home.jinja2')
