import websockets

from .WebsocketSubscription import WebsocketSubscription

class WebsocketsClient:
    
    def __init__(self, url):
        self.__id = 0
        self.__url = url
        self.__sockets = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        for socket in self.__sockets:
            self.socket.__exit__(exc_type, exc_value, traceback)

    def subscription(
        self,
        query,
        variables=None,
        operationName=None,
        parser=None,
        reconnect=True):

        self.__id = self.__id + 1
        socket = WebsocketSubscription(
            self.__id,
            self.__url,
            query,
            variables,
            operationName,
            parser,
            reconnect)

        return socket.subscribe()