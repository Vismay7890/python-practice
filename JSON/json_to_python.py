import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y)
print(type(y))