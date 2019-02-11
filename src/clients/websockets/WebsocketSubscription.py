from .Constants import Keys
from .Messages import Messages

class WebsocketSubscription:

    def __init__(self, url, query, variables=None):
        self.__socket = None

    def __enter__(self):
        self.__socket.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        self.__socket.__exit__()

    async def __init_socket(self):
        if self.__socket:
            return

        self.__socket = websockets.connect(uri, create_protocol=protocol)
        await self.__socket.send(Message.CONNECTION_INIT)

    def subscribe(self):

        def self.__init_socket()

        async for _message in self.__socket:

            message = json.loads(_message)

            if message[Keys.K_TYPE] == Keys.K_TYPE:
                await websocket.send()