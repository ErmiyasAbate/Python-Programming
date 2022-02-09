i = 1
j = 1
k = 1

while i <= 6:
    print(i)
    i += 1
else:
    print("i is greater than 6")


while j <= 6:
    print(j)
    if j == 3:
        break
    j += 1

while k <= 6:
    k += 1
    if k == 3:
        continue
    print(k)