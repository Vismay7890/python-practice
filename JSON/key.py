import json
sample = """{"key1": "value1", "key2": "value2"}"""
y = json.loads(sample)
print(y['key2'])