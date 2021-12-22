tup = ("hi", "Python", 2)
print(type(tup))
print(tup)

# Tuple Slicing
print(tup[1:])
print(tup[1:2])
print(tup[0:2])

# Tuple concatenation using + operator
print(tup + tup)

# Tuple reputation using * operator
print(tup * 3)

tup[2] = "hello"
