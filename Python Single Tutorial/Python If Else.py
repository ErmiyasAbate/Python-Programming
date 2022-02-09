a = 200
b = 33
c = 500

if a > b:
    print("a is greater than b!")
elif b > a:
    print("b is greater than a!")
else:
    print("a and b are equal!")

# Short Hand If... Else
print("a is greater than b!") if a > b else print("b is greater than a!")

print("a is greater than b!") if a > b else print("b is greater than a!") if a < b else print("a and b are equal!")

if a > b and c > a:
    print("Both conditions are True")
elif a > b or a > c:
    print("At least one of the conditions is True")

x = 41

if x > 10:
    print("41 is above ten,", end=" ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20!")

