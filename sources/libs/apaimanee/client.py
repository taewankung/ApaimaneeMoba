from apmn_client import client as aclient
from .game_logic import GameLogic

class Singleton(type):
    def __init__(cls,name,bases,dic):
        super(Singleton,cls).__init__(name, bases, dic)
        cls.instance=None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance=super(Singleton,cls).__call__(*args, **kw)
        return cls.instance


class ApaimaneeMOBAClient(metaclass=Singleton):
    def __init__(self, client_id,
            host='localhost', port='1883',
            room_id=None):
        self._client_id = client_id
        self._host = host
        self._port = port
        self._room_id = room_id
        self.game_client = None
        self.game_logic = GameLogic()

    def connect(self):
        if self.game_client is None:

            self.game_client = aclient.ApaimaneeClient(self._client_id,
                    self._host, self._port)
            self.game_client.initial()
            self.game_client.gm.start_game(self._room_id)
            self.game_client.gm.register(self.game_logic)

    def disconnect(self):
        self.game_client.disconnect()


