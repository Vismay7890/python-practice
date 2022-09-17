import json
from types import SimpleNamespace

vehicle = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'
class Vehicle:
    def __init__(self,name,engine,price):
        self.name = name
        self.engine = engine
        self.price = price
# c1 = json.loads(vehicle,object_hook = lambda d: SimpleNamespace(**d))
# print(c1.name,c1.engine,c1.price)
c1 = json.loads(vehicle)
v = Vehicle(**c1)
print(v.name)