import json

from .Constants import Keys, Types

class Message:

    CONNECTION_INIT = json.dumps({
        [Keys.K_TYPE]: Types.CONNECTION_ACK,
        [Keys.K_PAYLOAD]: {}
    })

    def create_query(id, type, query, variables):
        return {
            [Keys.K_ID]: Types.START
        }
