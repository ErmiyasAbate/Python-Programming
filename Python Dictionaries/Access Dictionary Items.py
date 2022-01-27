thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])

print(thisdict.get("brand"))
print(thisdict.get("model"))
print(thisdict.get("year"))

print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
