fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

"""
If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be assigned to the 
variable as a list:
"""
x = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = x
print(green)
print(yellow)
print(red)

(green, *tropic, red) = x
print(green)
print(tropic)
print(red)
