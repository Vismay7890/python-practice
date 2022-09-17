import json
x = """ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
"""
y =[]
try:
    y = json.loads(x)
except Exception as e:
    print(e)
data = [item.get('name') for item in y]
print(data)