a = ("a", "b", "c", "d")
print(a)
print(len(a))

# To Create a tuple with a single item with must add a comma after the item
b = ("b",)
print(type(b))

c = (1, 2, 3, 4)
d = (True, False, False)
print(c)
print(d)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# It is also possible to use the tuple() constructor to make a tuple.
e = tuple(("a"))
print(type(e))

print(tuple1[-1])

if False in tuple1:
    print("It is available")
else:
    print("It is not available")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
