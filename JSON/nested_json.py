import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
x = json.loads(sampleJson)
print("Salary is: ",x["company"]["employee"]["payble"]["salary"])