list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

a = ["a", "b", "c"]
b = [1, 2, 3]
a.extend(b)
print(a)

c = ["a", "b", "c"]
d = [1, 2, 3]

for x in d:
    c.append(x)
print(c)
