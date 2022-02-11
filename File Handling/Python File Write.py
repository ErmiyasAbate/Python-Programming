f = open("demofile2.txt", "a")
f.write("\nNow the file has more content!")
f.close()

f = open("demofile2.txt")
print(f.read())
f.close()