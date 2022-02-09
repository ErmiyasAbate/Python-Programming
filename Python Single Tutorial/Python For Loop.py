fruites = ["apple", "banana", "cherry"]

for i in fruites:
    print(i)

for i in range(len(fruites)):
    print(i)

for i in "banana":
    print(i, end=" ")

print()

for j in fruites:
    print(j)
    if j == "banana":
        break

for a in range(6):
    print(a)

print()

for b in range(2,6):
    print(b)

print()

for b in range(2,30, 3):
    print(b)

print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, " ", y)
