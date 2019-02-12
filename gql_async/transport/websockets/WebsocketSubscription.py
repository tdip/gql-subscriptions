from graphql.execution import ExecutionResult
import json
import websockets

from .Constants import Keys
from .Events import Events
from .Message import Message
from .Protocol import protocol

class WebsocketSubscription:

    def __init__(self, id, url, query, variables=None, operationName=None):
        self.__id = id
        self.__url = url
        self.__query = query
        self.__variables = variables
        self.__operationName = operationName
        self.__socket = None

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
                await self.__socket.send(
                    Message.create_query(
                        self.__id,
                        self.__query,
                        self.__variables,
                        self.__operationName))

            if type == Events.DATA:

                payload = message.get(Keys.PAYLOAD)
                data = payload.get(Keys.DATA)
                errors = payload.get(Keys.ERRORS)

                yield ExecutionResult(data=data, errors=errors)

            print(_message)
            print("message:", message)