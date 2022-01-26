set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = {"b", "c", "d"}

set4 = set1.union(set2)
print(set4)

set1.update(set2)
print(set1)

a = set1.intersection(set3)
b = set2.intersection(set3)
print(a)
print(b)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
x1.symmetric_difference_update(y1)
print(x1)

x11 = {1, 2, 3, 4}
y11 = {3, 4, 5, 6}
z11 = x11.symmetric_difference(y11)
print(z11)
