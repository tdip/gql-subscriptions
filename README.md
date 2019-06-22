# gql-subscriptions
A simple GQL python client that supports subscriptions

## Sample usage:
```
from gql_async import Client

client = Client('ws://my_endpoint')

async for message in client.subscribe('subscription{...}'):
    do_something_with_message(message)

```

Messages will be provided as an instance of the `ExcecutionResult` class
which comes from the "graphql-core" library.
