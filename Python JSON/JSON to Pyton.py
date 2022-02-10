import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print("My name is " + y["name"])
print("I'm",  y["age"], "years old")
print("and I live in " + y["city"])