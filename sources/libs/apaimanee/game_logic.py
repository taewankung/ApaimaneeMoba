

class GameLogic:
    def __init__(self):
        self.status = 'wait'
        self.heros = dict()

    def start_game(self):
        self.status = 'play'

    def initial_game(self, args):
        for hero in args['heros']:
            self.heros[hero.id] = hero
