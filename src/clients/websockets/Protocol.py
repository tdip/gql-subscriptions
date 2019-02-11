from websockets.client import WebSocketClientProtocol

def protocol(*args, **kwargs):
    kwargs['subprotocols'] = ['graphql-subscriptions']
    return WebSocketClientProtocol(*args, **kwargs)