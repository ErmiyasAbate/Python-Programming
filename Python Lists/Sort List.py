a = ["orange", "mango", "kiwi", "pineapple", "banana"]
a.sort()
print(a)

b = [100, 50, 65, 82, 23]
b.sort()
print(b)
print()

c = ["orange", "mango", "kiwi", "pineapple", "banana"]
c.sort(reverse=True)
print(c)

d = [100, 50, 65, 82, 23]
d.sort(reverse=True)
print(d)
print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist.sort(key=str.lower)
print(thislist)
