thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.pop("model")
thisdict.popitem()
print(thisdict)

cars = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
cars.clear()
print(cars)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del car["model"]
print(car)
