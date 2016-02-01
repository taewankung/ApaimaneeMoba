from apmn_client import client as aclient


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

        self.game_client = aclient.ApaimaneeClient(client_id, host, port)


