import json

from .Constants import Keys, Types

class Message:

    CONNECTION_INIT = json.dumps({
        Keys.TYPE: Types.CONNECTION_INIT,
        Keys.PAYLOAD: {}
    })

    def create_query_message(id, query, variables=None, operationName=None):

        payload = {
            Keys.QUERY: query
        }

        if variables:
            payload[Keys.VARIABLES] = variables

        result = {
            Keys.ID: id,
            Keys.TYPE: Types.START,
            Keys.PAYLOAD: payload
        }

        if operationName:
            result[Keys.OPERATION_NAME] = operationName

        return result

    def create_query(id, query, variables, operationName):
        return json.dumps(Message.create_query_message(id, query, variables, operationName))