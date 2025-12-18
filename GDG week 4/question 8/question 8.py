import json

user = {
    "username": "dagim",
    "email": "dagim@gmail.com",
    "active": True
}

json_string =json.dumps(user)

print(json_string)