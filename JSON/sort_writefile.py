import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
print("Writing json file:")
with open("sampleJson.json","w") as write_file:
    write_file.write(json.dumps(sampleJson,indent=4,sort_keys=True))
print("File write done")