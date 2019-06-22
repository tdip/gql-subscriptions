from graphql.language.printer import print_ast

from .errors.GQLClientErrorBase import GQLClientErrorBase
from .transport.websockets.WebsocketsClient import WebsocketsClient

class Client:
    '''
    A GraphQL client that supports subscribing to endpints via websockets
    '''
    def __init__(self, subscription_endpoint=None):

        self.__websockets = WebsocketsClient(subscription_endpoint) if subscription_endpoint else None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.__websockets:
            self.__websockets.__exit__(exc_type, exc_value, traceback)

    def subscribe(self, query, variables=None, parser=None, reconnect=True):
        '''
        Subscribe to the resulsts of executing the argument query.
        :param query: The GraphQL query to execute
        :type query: str

        :param variables: The GraphQL variables binding to the given query
        :type variables: dict

        :param parser: The parser that should be used to parse the payload 
        from the gql endpoint
        :type parser: function

        :return An async iterator that yields the values from the endpoint
        '''
        if not self.__websockets:
            raise GQLClientErrorBase("Missing websocket endpoint.")

        return self.__websockets.subscription(
            query,
            variables=variables,
            parser=parser,
            reconnect=reconnect)

    