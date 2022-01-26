x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

# Adding item
z = list(x)
z.append("Mango")
x = tuple(z)
print(x)

a = ("Orange", "Banana")
x += a
print(x)
