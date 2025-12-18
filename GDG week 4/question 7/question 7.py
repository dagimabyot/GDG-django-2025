import json

json_data = '''
{
  "product": "Laptop",
  "price": 75000,
  "avaliable": "True"
}
'''

data = json.loads(json_data)

print(data["product"])
print(data["price"])
