thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x)

print()

for x in thisdict:
    print(thisdict[x])

print()

for x in thisdict.values():
    print(x)

print()

for x,y in thisdict.items():
    print(x, " = ", y)
