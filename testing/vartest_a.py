from pymemcache.client.base import Client
client = Client(('localhost', 11211))
val = input('enter a value')
client.set('some_key', val)
print(val)
