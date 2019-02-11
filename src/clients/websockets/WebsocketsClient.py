import websockets

from .WebsocketSubscription import WebsocketSubscription

class WebsocketsClient:
    
    def __init__(self, uri):
        self.uri = uri
        self.sockets = []

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):

        for socket in self.sockets:
            self.socket.__exit__(exc_type, exc_value, traceback)

    def subscription(query, variables):
        pass