thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
thisset.discard("banana")
print(thisset)

a = {"apple", "banana", "cherry"}
x = a.pop() # Remove the last item by using the pop() method:
print(x)
print(a)

b = {"apple", "banana", "cherry"}
b.clear()
print(b)

c = {"apple", "banana", "cherry"}
del c
print(c)
