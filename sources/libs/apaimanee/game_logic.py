
class GameLogic:
    def __init__(self, game_client):
        self.status = 'wait'
        self.heros = dict()
        self.players = None

        self.game_client = game_client

    def start_game(self):
        self.status = 'play'

    def initial_game(self, players):
        if players is None:
            return

        self.players = players
        self.game_client.game.ready()


