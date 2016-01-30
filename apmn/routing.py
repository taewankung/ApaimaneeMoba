'''
Created on Dec 3, 2012

@author: superizer
'''
from .views import accounts, games

def add_route(config):
    config.add_route('index', '/', accounts.login, '/accounts/login.jinja2')
    config.add_route('login', '/login', accounts.login, '/accounts/login.jinja2')
    config.add_route('home', '/home', accounts.home, '/accounts/home.jinja2')
    config.add_route('register', '/register', accounts.register, '/accounts/register.jinja2')
    config.add_route('games.create_room', '/games/create_room', games.create_room, '/accounts/create_room.jinja2')
    config.add_route('games.room', '/games/room', games.room, '/accounts/room.jinja2')
