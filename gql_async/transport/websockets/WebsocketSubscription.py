from graphql.execution import ExecutionResult
import json
import websockets

from .Constants import Keys
from .Events import Events
from .Message import Message
from .Protocol import protocol

def default_parser(payload):
    data = payload.get(Keys.DATA)
    errors = payload.get(Keys.ERRORS)

    return ExecutionResult(data=data, errors=errors)

class WebsocketSubscription:

    def __init__(self, id, url, query, variables=None, operationName=None, parser=None):
        self.__id = id
        self.__url = url
        self.__query = query
        self.__variables = variables
        self.__operationName = operationName
        self.__socket = None
        self.__parser = parser if parser else default_parser

    def __enter__(self):
        self.__socket.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        self.__socket.__exit__()

    async def __init_socket(self):
        if self.__socket:
            return

        self.__socket = await websockets.connect(self.__url, create_protocol=protocol)
        await self.__socket.send(Message.CONNECTION_INIT)
        print(Message.CONNECTION_INIT)

    async def subscribe(self):

        await self.__init_socket()

        async for _message in self.__socket:

            message = json.loads(_message)
            type = message[Keys.TYPE]

            if type == Events.CONNECTION_ACK:

                query = Message.create_query(
                    self.__id,
                    self.__query,
                    self.__variables,
                    self.__operationName)

                await self.__socket.send(query)

            if type == Events.DATA:

                payload = message.get(Keys.PAYLOAD)
                yield self.__parser(payload)