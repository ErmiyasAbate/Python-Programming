import json

x = {
    "name":"Ermiyas",
    "age": 25,
    "city": "Addis Ababa"
}

y = json.dumps(x)

print(y)