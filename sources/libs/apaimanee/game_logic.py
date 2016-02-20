
class GameLogic:
    def __init__(self, game_client):
        self.status = 'wait'
        self.heros = dict()
        self.players = None

        self.game_space = None
        self.game_client = game_client

    def start_game(self):
        self.status = 'play'


    def initial_game(self, players, game_space):
        if players is None:
            return
        self.game_space = game_space
        self.players = players
        self.game_client.game.ready()


