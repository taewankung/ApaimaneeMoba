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
    config.add_route('games.create_room', '/games/create_room', games.create_room, '/games/create_room.jinja2')
    config.add_route('games.room', '/games/room', games.room, '/games/room.jinja2')
    config.add_route('games.select_hero', '/games/select_hero', games.select_hero,'/games/select_hero.jinja2')
    config.add_route('games.join_game', '/games/join_game', games.join_game, None)
    config.add_route('games.load_game', '/games/load_game', games.load_game, '/games/load_game.jinja2')
