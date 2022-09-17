import json
sample = {"key1": "value1", "key2": "value2"}
y = json.dumps(sample , indent=2 , separators = (",","="))
print(y)