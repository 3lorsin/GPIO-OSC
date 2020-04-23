from pymemcache.client.base import Client
client = Client(('localhost', 11211))
result = client.get('some_key')
print(result)
